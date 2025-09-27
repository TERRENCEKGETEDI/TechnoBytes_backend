from flask import Blueprint, request, jsonify
from models import db, ServiceRequest, Service, Notification
from middleware.auth import jwt_required_custom
from datetime import datetime

requests_bp = Blueprint('requests', __name__)

@requests_bp.route('', methods=['GET'])
@jwt_required_custom
def get_requests(user):
    status = request.args.get('status')
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)

    query = ServiceRequest.query.filter(
        (ServiceRequest.customer_id == user.id) | (ServiceRequest.provider_id == user.id)
    )

    if status:
        query = query.filter_by(status=status)

    requests = query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        'success': True,
        'data': {
            'requests': [r.to_dict() for r in requests.items],
            'pagination': {
                'page': page,
                'limit': limit,
                'total': requests.total,
                'pages': requests.pages
            }
        }
    })

@requests_bp.route('', methods=['POST'])
@jwt_required_custom
def create_request(user):
    data = request.get_json()
    service_id = data.get('service_id')
    message = data.get('message')
    requested_date = data.get('requested_date')
    estimated_duration = data.get('estimated_duration')

    if not service_id:
        return jsonify({'success': False, 'error': 'Service ID is required'}), 400

    service = Service.query.filter_by(id=service_id, is_active=True).first()
    if not service:
        return jsonify({'success': False, 'error': 'Service not found'}), 404

    if service.provider_id == user.id:
        return jsonify({'success': False, 'error': 'Cannot request your own service'}), 400

    request_obj = ServiceRequest(
        service_id=service_id,
        customer_id=user.id,
        provider_id=service.provider_id,
        message=message,
        requested_date=datetime.fromisoformat(requested_date) if requested_date else None,
        estimated_duration=estimated_duration,
        customer_phone=user.phone,
        customer_email=user.email
    )
    db.session.add(request_obj)
    db.session.commit()

    # Create notification for provider
    notification = Notification(
        user_id=service.provider_id,
        type='request',
        title='New Service Request',
        message=f'{user.name} has requested your service: {service.title}',
        data={'request_id': request_obj.id}
    )
    db.session.add(notification)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': request_obj.to_dict(),
        'message': 'Service request created successfully'
    }), 201

@requests_bp.route('/<request_id>', methods=['PATCH'])
@jwt_required_custom
def update_request_status(user, request_id):
    data = request.get_json()
    status = data.get('status')

    if status not in ['accepted', 'declined']:
        return jsonify({'success': False, 'error': 'Invalid status'}), 400

    request_obj = ServiceRequest.query.get(request_id)
    if not request_obj:
        return jsonify({'success': False, 'error': 'Request not found'}), 404

    if request_obj.provider_id != user.id:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403

    request_obj.status = status
    db.session.commit()

    # Create notification for customer
    notification = Notification(
        user_id=request_obj.customer_id,
        type='acceptance' if status == 'accepted' else 'decline',
        title=f'Request {status.capitalize()}',
        message=f'Your service request for {request_obj.service.title} has been {status}',
        data={'request_id': request_obj.id}
    )
    db.session.add(notification)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': request_obj.to_dict(),
        'message': f'Request {status} successfully'
    })