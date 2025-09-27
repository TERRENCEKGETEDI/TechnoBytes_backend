from flask import Blueprint, request, jsonify
from models import db
from middleware.auth import jwt_required_custom

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('', methods=['GET'])
@jwt_required_custom
def get_profile(user):
    return jsonify({
        'success': True,
        'data': user.to_dict()
    })

@profile_bp.route('', methods=['PATCH'])
@jwt_required_custom
def update_profile(user):
    data = request.get_json()
    allowed_fields = ['name', 'phone', 'location']

    for field in allowed_fields:
        if field in data:
            setattr(user, field, data[field])

    db.session.commit()
    return jsonify({
        'success': True,
        'data': user.to_dict(),
        'message': 'Profile updated successfully'
    })