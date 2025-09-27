from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
import bcrypt
import uuid
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum('customer', 'provider', name='user_role'), nullable=False)
    phone = db.Column(db.String(20))
    location = db.Column(db.String(255))
    avatar_url = db.Column(db.String(500))
    rating = db.Column(db.Numeric(3, 2), default=0.00)
    is_verified = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    services = db.relationship('Service', backref='provider', lazy=True)
    sent_requests = db.relationship('ServiceRequest', backref='customer', lazy=True, foreign_keys='ServiceRequest.customer_id')
    received_requests = db.relationship('ServiceRequest', backref='provider_rel', lazy=True, foreign_keys='ServiceRequest.provider_id')
    feedbacks_given = db.relationship('Feedback', backref='customer', lazy=True, foreign_keys='Feedback.customer_id')
    feedbacks_received = db.relationship('Feedback', backref='provider', lazy=True, foreign_keys='Feedback.provider_id')
    notifications = db.relationship('Notification', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'phone': self.phone,
            'location': self.location,
            'avatar_url': self.avatar_url,
            'rating': float(self.rating) if self.rating else 0.0,
            'is_verified': self.is_verified,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ServiceCategory(db.Model):
    __tablename__ = 'service_categories'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), unique=True, nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    services = db.relationship('Service', backref='category', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon,
            'color': self.color,
            'description': self.description,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    provider_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.String(36), db.ForeignKey('service_categories.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2))
    price_type = db.Column(Enum('hourly', 'fixed', 'negotiable', name='price_type'), nullable=False)
    images = db.Column(db.JSON)
    rating = db.Column(db.Numeric(3, 2), default=0.00)
    review_count = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    requests = db.relationship('ServiceRequest', backref='service', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category.to_dict() if self.category else None,
            'provider': {
                'id': self.provider.id,
                'name': self.provider.name,
                'rating': float(self.provider.rating) if self.provider.rating else 0.0,
                'location': self.provider.location
            },
            'location': self.location,
            'price': float(self.price) if self.price else None,
            'price_type': self.price_type,
            'images': self.images or [],
            'rating': float(self.rating) if self.rating else 0.0,
            'review_count': self.review_count,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    service_id = db.Column(db.String(36), db.ForeignKey('services.id'), nullable=False)
    customer_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    status = db.Column(Enum('pending', 'accepted', 'declined', 'completed', 'cancelled', name='request_status'), default='pending')
    message = db.Column(db.Text)
    requested_date = db.Column(db.Date)
    estimated_duration = db.Column(db.Integer)
    customer_phone = db.Column(db.String(20))
    customer_email = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    feedback = db.relationship('Feedback', backref='service_request', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'service': {
                'id': self.service.id,
                'title': self.service.title,
                'provider': {
                    'id': self.service.provider.id,
                    'name': self.service.provider.name
                }
            },
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name
            },
            'provider': {
                'id': self.provider_rel.id,
                'name': self.provider_rel.name
            },
            'status': self.status,
            'message': self.message,
            'requested_date': self.requested_date.isoformat() if self.requested_date else None,
            'estimated_duration': self.estimated_duration,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    service_request_id = db.Column(db.String(36), db.ForeignKey('service_requests.id'), nullable=False)
    customer_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    is_public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name
            },
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    type = db.Column(Enum('request', 'acceptance', 'decline', 'completion', 'feedback', 'system', name='notification_type'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    data = db.Column(db.JSON)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class RefreshToken(db.Model):
    __tablename__ = 'refresh_tokens'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    token = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref='refresh_tokens', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'token': self.token,
            'user_id': self.user_id,
            'expires_at': self.expires_at.isoformat() if self.expires_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'message': self.message,
            'data': self.data,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }