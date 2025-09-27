from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from models import db, User, RefreshToken
from schemas import UserRegistrationSchema, UserLoginSchema
from limiter import limiter
import secrets
from datetime import datetime, timedelta

class RefreshTokenManager:
    @staticmethod
    def generate_refresh_token():
        """Generate a secure random refresh token"""
        return secrets.token_urlsafe(32)

    @staticmethod
    def store_refresh_token(user_id, refresh_token, expires_at):
        """Store refresh token with expiration"""
        # Revoke existing refresh tokens for this user
        RefreshToken.query.filter_by(user_id=user_id).delete()

        token = RefreshToken(
            token=refresh_token,
            user_id=user_id,
            expires_at=expires_at
        )
        db.session.add(token)
        db.session.commit()

    @staticmethod
    def validate_refresh_token(refresh_token):
        """Validate refresh token and return user_id if valid"""
        token = RefreshToken.query.filter_by(token=refresh_token).first()
        if not token:
            return None

        # Check if token has expired
        if datetime.utcnow() > token.expires_at:
            # Remove expired token
            db.session.delete(token)
            db.session.commit()
            return None

        return token.user_id

    @staticmethod
    def revoke_refresh_token(refresh_token):
        """Revoke a refresh token"""
        token = RefreshToken.query.filter_by(token=refresh_token).first()
        if token:
            db.session.delete(token)
            db.session.commit()

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per minute")
def register():
    data = request.get_json()
    schema = UserRegistrationSchema()
    try:
        validated_data = schema.load(data)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

    name = validated_data.get('name')
    email = validated_data.get('email')
    password = validated_data.get('password')
    role = validated_data.get('role', 'customer')
    phone = validated_data.get('phone')
    location = validated_data.get('location')

    existing = User.query.filter_by(email=email).first()
    if existing:
        return jsonify({'success': False, 'error': 'Email already in use'}), 409

    user = User(name=name, email=email, phone=phone, location=location, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity={'id': user.id})
    refresh_token = RefreshTokenManager.generate_refresh_token()
    refresh_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_REFRESH_TOKEN_EXPIRES'])
    RefreshTokenManager.store_refresh_token(user.id, refresh_token, refresh_expires)
    access_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    expires_in = int((access_expires - datetime.utcnow()).total_seconds())

    return jsonify({
        'success': True,
        'data': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': expires_in,
            'user': user.to_dict()
        },
        'message': 'User registered successfully'
    }), 201

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("10 per minute")
def login():
    data = request.get_json()
    schema = UserLoginSchema()
    try:
        validated_data = schema.load(data)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

    email = validated_data.get('email')
    password = validated_data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'id': user.id})
    refresh_token = RefreshTokenManager.generate_refresh_token()
    refresh_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_REFRESH_TOKEN_EXPIRES'])
    RefreshTokenManager.store_refresh_token(user.id, refresh_token, refresh_expires)
    access_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    expires_in = int((access_expires - datetime.utcnow()).total_seconds())

    return jsonify({
        'success': True,
        'data': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': expires_in,
            'user': user.to_dict()
        },
        'message': 'Login successful'
    })

@auth_bp.route('/refresh', methods=['POST'])
def refresh_token():
    """
    Refresh access token using refresh token

    Expected JSON payload:
    {
        "refresh_token": "your_refresh_token_here"
    }

    Returns:
    {
        "success": true,
        "data": {
            "access_token": "new_access_token",
            "refresh_token": "new_refresh_token",
            "expires_in": 900
        },
        "message": "Token refreshed successfully"
    }
    """
    try:
        data = request.get_json()

        if not data or 'refresh_token' not in data:
            return jsonify({
                'success': False,
                'message': 'Refresh token is required',
                'data': None
            }), 400

        refresh_token = data['refresh_token']

        # Validate refresh token
        user_id = RefreshTokenManager.validate_refresh_token(refresh_token)

        if not user_id:
            return jsonify({
                'success': False,
                'message': 'Invalid or expired refresh token',
                'data': None
            }), 401

        # Revoke the old refresh token
        RefreshTokenManager.revoke_refresh_token(refresh_token)

        # Create new access token
        access_token = create_access_token(
            identity={'id': user_id},
            additional_claims={
                'type': 'access',
                'user_id': user_id
            }
        )

        # Create new refresh token
        new_refresh_token = RefreshTokenManager.generate_refresh_token()

        # Calculate expiration times
        access_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
        refresh_expires = datetime.utcnow() + timedelta(seconds=current_app.config['JWT_REFRESH_TOKEN_EXPIRES'])

        # Store new refresh token
        RefreshTokenManager.store_refresh_token(
            user_id,
            new_refresh_token,
            refresh_expires
        )

        # Calculate expires_in in seconds
        expires_in = int((access_expires - datetime.utcnow()).total_seconds())

        return jsonify({
            'success': True,
            'data': {
                'access_token': access_token,
                'refresh_token': new_refresh_token,
                'expires_in': expires_in
            },
            'message': 'Token refreshed successfully'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error refreshing token: {str(e)}',
            'data': None
        }), 500