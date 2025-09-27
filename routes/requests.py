from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, ServiceRequest, Service, Payment, JobStat
from datetime import datetime

requests_bp = Blueprint('requests', __name__)

@requests_bp.route('/', methods=['POST'])
@jwt_required()
def create_request():
    current_user = get_jwt_identity()
    data = request.get_json()
    serviceId = data.get('serviceId')
    requestType = data.get('requestType')
    scheduledTime = data.get('scheduledTime')

    req_obj = ServiceRequest(
        customerId=current_user['id'],
        serviceId=serviceId,
        requestType=requestType,
        scheduledTime=scheduledTime
    )
    db.session.add(req_obj)
    db.session.commit()

    return jsonify(req_obj.to_dict())

@requests_bp.route('/<int:id>/accept', methods=['POST'])
@jwt_required()
def accept_request(id):
    current_user = get_jwt_identity()
    req = ServiceRequest.query.filter_by(id=id).first()
    if not req:
        return jsonify({'error': 'Request not found'}), 404

    service = Service.query.get(req.serviceId)
    if not service or service.providerId != current_user['id']:
        return jsonify({'error': 'Not allowed'}), 403

    req.status = 'accepted'
    db.session.commit()

    return jsonify(req.to_dict())

@requests_bp.route('/<int:id>/complete', methods=['POST'])
@jwt_required()
def complete_request(id):
    current_user = get_jwt_identity()
    req = ServiceRequest.query.filter_by(id=id).first()
    if not req:
        return jsonify({'error': 'Request not found'}), 404

    service = Service.query.get(req.serviceId)
    if not service or service.providerId != current_user['id']:
        return jsonify({'error': 'Not allowed'}), 403

    req.status = 'completed'
    req.completedAt = datetime.utcnow()
    db.session.commit()

    # Create payment
    payment = Payment(
        requestId=req.id,
        customerId=req.customerId,
        providerId=service.providerId,
        amount=service.price,
        status='completed'
    )
    db.session.add(payment)

    # Update JobStat
    job_stat = JobStat.query.filter_by(providerId=service.providerId).first()
    if job_stat:
        job_stat.totalJobs += 1
        job_stat.totalEarnings = float(job_stat.totalEarnings or 0) + float(payment.amount or 0)
        db.session.commit()

    return jsonify({'request': req.to_dict(), 'payment': payment.to_dict()})