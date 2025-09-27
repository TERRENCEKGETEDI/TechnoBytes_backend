from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, decode_token
from flask_socketio import SocketIO, emit, join_room
from models import db, Message
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Import blueprints
from routes.auth import auth_bp
from routes.services import services_bp
from routes.requests import requests_bp
from routes.messages import messages_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(services_bp, url_prefix='/api/services')
app.register_blueprint(requests_bp, url_prefix='/api/requests')
app.register_blueprint(messages_bp, url_prefix='/api/messages')

@app.route('/')
def health_check():
    return jsonify({'ok': True})

# SocketIO events
@socketio.on('connect')
def handle_connect():
    token = request.args.get('token')  # or from handshake auth
    if not token:
        return False
    try:
        payload = decode_token(token)
        user_id = payload['sub']['id']
        join_room(f"user:{user_id}")
        print(f'Client {user_id} connected')
    except:
        return False

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send_message')
def handle_send_message(data):
    token = request.args.get('token')
    if not token:
        return
    try:
        payload = decode_token(token)
        user_id = payload['sub']['id']
        conversation_id = data.get('conversationId')
        message_text = data.get('messageText')
        if not conversation_id or not message_text:
            return
        msg = Message(conversationId=conversation_id, senderId=user_id, messageText=message_text)
        db.session.add(msg)
        db.session.commit()
        emit('message', msg.to_dict(), room=f"conversation:{conversation_id}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # For dev, create tables
    port = int(os.environ.get('PORT', 4000))
    socketio.run(app, host='0.0.0.0', port=port, debug=app.config['FLASK_ENV'] == 'development')