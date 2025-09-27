from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User, JobStat
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    fullName = data.get('fullName')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    password = data.get('password')
    role = data.get('role', 'customer')

    if not all([fullName, email, phoneNumber, password]):
        return jsonify({'error': 'Missing fields'}), 400

    existing = User.query.filter_by(email=email).first()
    if existing:
        return jsonify({'error': 'Email already in use'}), 409

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(fullName=fullName, email=email, phoneNumber=phoneNumber, passwordHash=password_hash, role=role)
    db.session.add(user)
    db.session.commit()

    if user.role == 'provider':
        job_stat = JobStat(providerId=user.id)
        db.session.add(job_stat)
        db.session.commit()

    access_token = create_access_token(identity={'id': user.id, 'role': user.role})
    return jsonify({
        'token': access_token,
        'user': {'id': user.id, 'fullName': user.fullName, 'email': user.email, 'role': user.role}
    })

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email/password'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity={'id': user.id, 'role': user.role})
    return jsonify({
        'token': access_token,
        'user': {'id': user.id, 'fullName': user.fullName, 'email': user.email, 'role': user.role}
    })