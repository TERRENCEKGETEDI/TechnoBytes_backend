from flask import Blueprint, request, jsonify
from models import Service, ServiceCategory
from middleware.auth import jwt_required_custom
from sqlalchemy import or_, and_

services_bp = Blueprint('services', __name__)

@services_bp.route('', methods=['GET'])
def get_services():
    # Query parameters
    category = request.args.get('category')
    location = request.args.get('location')
    search = request.args.get('search')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)

    query = Service.query.filter_by(is_active=True)

    if category:
        query = query.filter_by(category_id=category)
    if location:
        query = query.filter(Service.location.ilike(f'%{location}%'))
    if search:
        query = query.filter(or_(
            Service.title.ilike(f'%{search}%'),
            Service.description.ilike(f'%{search}%')
        ))
    if min_price is not None:
        query = query.filter(Service.price >= min_price)
    if max_price is not None:
        query = query.filter(Service.price <= max_price)

    services = query.paginate(page=page, per_page=limit, error_out=False)
    total = services.total
    pages = services.pages

    return jsonify({
        'success': True,
        'data': {
            'services': [s.to_dict() for s in services.items],
            'pagination': {
                'page': page,
                'limit': limit,
                'total': total,
                'pages': pages
            }
        }
    })

@services_bp.route('/<service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.filter_by(id=service_id, is_active=True).first()
    if not service:
        return jsonify({'success': False, 'error': 'Service not found'}), 404

    return jsonify({
        'success': True,
        'data': service.to_dict()
    })

@services_bp.route('', methods=['POST'])
@jwt_required_custom
def create_service(user):
    if user.role != 'provider':
        return jsonify({'success': False, 'error': 'Only providers can create services'}), 403

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    category_id = data.get('category')
    location = data.get('location')
    price = data.get('price')
    price_type = data.get('price_type')
    images = data.get('images', [])

    if not all([title, description, category_id, location, price_type]):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    category = ServiceCategory.query.get(category_id)
    if not category:
        return jsonify({'success': False, 'error': 'Invalid category'}), 400

    service = Service(
        provider_id=user.id,
        category_id=category_id,
        title=title,
        description=description,
        location=location,
        price=price,
        price_type=price_type,
        images=images
    )
    from models import db
    db.session.add(service)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': service.to_dict(),
        'message': 'Service created successfully'
    }), 201