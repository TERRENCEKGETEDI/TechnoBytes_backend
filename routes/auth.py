from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'customer')
    phone = data.get('phone')
    location = data.get('location')

    if not all([name, email, password]):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

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
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'error': 'Missing email or password'}), 400

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