from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from flask import jsonify
from models import User

def jwt_required_custom(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        try:
            user_id = get_jwt_identity()['id']
            user = User.query.get(user_id)
            if not user:
                return jsonify({'success': False, 'error': 'User not found'}), 404
            return fn(user, *args, **kwargs)
        except Exception as e:
            return jsonify({'success': False, 'error': 'Invalid token'}), 401
    return wrapper