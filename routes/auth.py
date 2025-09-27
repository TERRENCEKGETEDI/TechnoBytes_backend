from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User
from schemas import UserRegistrationSchema, UserLoginSchema
from limiter import limiter

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
    return jsonify({
        'success': True,
        'data': {
            'token': access_token,
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
    return jsonify({
        'success': True,
        'data': {
            'token': access_token,
            'user': user.to_dict()
        },
        'message': 'Login successful'
    })