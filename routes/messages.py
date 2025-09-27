from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Conversation, Message

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/conversation', methods=['POST'])
@jwt_required()
def get_or_create_conversation():
    current_user = get_jwt_identity()
    data = request.get_json()
    requestId = data.get('requestId')
    customerId = data.get('customerId')
    providerId = data.get('providerId')

    conv = Conversation.query.filter_by(requestId=requestId).first()
    if not conv:
        conv = Conversation(requestId=requestId, customerId=customerId, providerId=providerId)
        db.session.add(conv)
        db.session.commit()

    return jsonify(conv.to_dict())

@messages_bp.route('/<int:conversationId>/message', methods=['POST'])
@jwt_required()
def post_message(conversationId):
    current_user = get_jwt_identity()
    data = request.get_json()
    messageText = data.get('messageText')

    msg = Message(conversationId=conversationId, senderId=current_user['id'], messageText=messageText)
    db.session.add(msg)
    db.session.commit()

    return jsonify(msg.to_dict())