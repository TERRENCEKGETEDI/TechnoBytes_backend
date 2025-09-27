from flask import Blueprint, request, jsonify
from models import db, Feedback, ServiceRequest, Notification
from middleware.auth import jwt_required_custom
from sqlalchemy import func

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('', methods=['POST'])
@jwt_required_custom
def submit_feedback(user):
    data = request.get_json()
    service_request_id = data.get('service_request_id')
    rating = data.get('rating')
    comment = data.get('comment')

    if not service_request_id or not rating:
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    if not (1 <= rating <= 5):
        return jsonify({'success': False, 'error': 'Rating must be between 1 and 5'}), 400

    request_obj = ServiceRequest.query.filter_by(
        id=service_request_id,
        customer_id=user.id,
        status='completed'
    ).first()

    if not request_obj:
        return jsonify({'success': False, 'error': 'Service request not found or not completed'}), 404

    if request_obj.feedback:
        return jsonify({'success': False, 'error': 'Feedback already submitted'}), 400

    feedback = Feedback(
        service_request_id=service_request_id,
        customer_id=user.id,
        provider_id=request_obj.provider_id,
        rating=rating,
        comment=comment
    )
    db.session.add(feedback)
    db.session.commit()

    # Update provider rating
    avg_rating = db.session.query(func.avg(Feedback.rating)).filter_by(provider_id=request_obj.provider_id).scalar()
    provider = request_obj.provider_rel
    provider.rating = float(avg_rating) if avg_rating else 0.0
    db.session.commit()

    # Create notification for provider
    notification = Notification(
        user_id=request_obj.provider_id,
        type='feedback',
        title='New Feedback Received',
        message=f'{user.name} left feedback for your service',
        data={'feedback_id': feedback.id}
    )
    db.session.add(notification)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': feedback.to_dict(),
        'message': 'Feedback submitted successfully'
    }), 201

@feedback_bp.route('/provider/<provider_id>', methods=['GET'])
def get_provider_feedback(provider_id):
    feedbacks = Feedback.query.filter_by(provider_id=provider_id, is_public=True).all()
    avg_rating = db.session.query(func.avg(Feedback.rating)).filter_by(provider_id=provider_id).scalar()
    total_reviews = len(feedbacks)

    return jsonify({
        'success': True,
        'data': {
            'feedback': [f.to_dict() for f in feedbacks],
            'average_rating': float(avg_rating) if avg_rating else 0.0,
            'total_reviews': total_reviews
        }
    })