from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Service, User
from sqlalchemy import or_

services_bp = Blueprint('services', __name__)

@services_bp.route('/', methods=['POST'])
@jwt_required()
def create_service():
    current_user = get_jwt_identity()
    if current_user['role'] != 'provider':
        return jsonify({'error': 'Only providers can create services'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')
    price = data.get('price')
    location = data.get('location')
    imageUrl = data.get('imageUrl')

    service = Service(
        providerId=current_user['id'],
        name=name,
        description=description,
        category=category,
        price=price,
        location=location,
        imageUrl=imageUrl
    )
    db.session.add(service)
    db.session.commit()

    return jsonify(service.to_dict())

@services_bp.route('/', methods=['GET'])
def list_services():
    category = request.args.get('category')
    location = request.args.get('location')
    q = request.args.get('q')

    query = Service.query

    if category:
        query = query.filter_by(category=category)
    if location:
        query = query.filter_by(location=location)
    if q:
        query = query.filter(Service.name.ilike(f'%{q}%'))

    services = query.all()
    result = []
    for service in services:
        service_dict = service.to_dict()
        provider = User.query.get(service.providerId)
        service_dict['provider'] = {
            'id': provider.id,
            'fullName': provider.fullName,
            'isVerified': provider.isVerified
        } if provider else None
        result.append(service_dict)

    return jsonify(result)