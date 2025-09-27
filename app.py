from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from limiter import limiter
import os

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, origins="*")
db.init_app(app)
jwt = JWTManager(app)
limiter.init_app(app)

# Import blueprints
from routes.auth import auth_bp
from routes.services import services_bp
from routes.requests import requests_bp
from routes.categories import categories_bp
from routes.feedback import feedback_bp
from routes.profile import profile_bp
from routes.verification import verification_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(services_bp, url_prefix='/api/services')
app.register_blueprint(requests_bp, url_prefix='/api/requests')
app.register_blueprint(categories_bp, url_prefix='/api/categories')
app.register_blueprint(feedback_bp, url_prefix='/api/feedback')
app.register_blueprint(profile_bp, url_prefix='/api/profile')
app.register_blueprint(verification_bp, url_prefix='/api/verification')

@app.route('/')
def health_check():
    return jsonify({'success': True, 'message': 'LinkLocal API is running'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # For dev, create tables
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=app.config['FLASK_ENV'] == 'development')