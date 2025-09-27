from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phoneNumber = db.Column(db.String(20), nullable=False, unique=True)
    passwordHash = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum('master', 'admin', 'provider', 'customer', name='user_role'), default='customer')
    isVerified = db.Column(db.Boolean, default=False)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # Relationships
    services = db.relationship('Service', backref='provider', lazy=True)
    service_requests = db.relationship('ServiceRequest', backref='customer', lazy=True, foreign_keys='ServiceRequest.customerId')
    job_stat = db.relationship('JobStat', backref='provider', uselist=False)
    messages = db.relationship('Message', backref='sender', lazy=True)
    admin_approvals = db.relationship('AdminApproval', backref='admin', lazy=True, foreign_keys='AdminApproval.adminId')
    password_resets = db.relationship('PasswordReset', backref='user', lazy=True)

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.passwordHash.encode('utf-8'))

    def to_dict(self):
        return {
            'id': self.id,
            'fullName': self.fullName,
            'email': self.email,
            'phoneNumber': self.phoneNumber,
            'role': self.role,
            'isVerified': self.isVerified,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

class Service(db.Model):
    __tablename__ = 'Services'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    providerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2))
    location = db.Column(db.String(255))
    imageUrl = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # Relationships
    service_requests = db.relationship('ServiceRequest', backref='service', lazy=True)
    reviews = db.relationship('Review', backref='service', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'providerId': self.providerId,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'price': float(self.price) if self.price else None,
            'location': self.location,
            'imageUrl': self.imageUrl,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

class ServiceRequest(db.Model):
    __tablename__ = 'ServiceRequests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    serviceId = db.Column(db.Integer, db.ForeignKey('Services.id'), nullable=False)
    requestType = db.Column(Enum('urgent', 'scheduled', name='request_type'), nullable=False)
    scheduledTime = db.Column(db.DateTime)
    status = db.Column(Enum('pending', 'accepted', 'completed', 'cancelled', name='request_status'), default='pending')
    completedAt = db.Column(db.DateTime)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'conversationId': self.conversationId,
            'senderId': self.senderId,
            'messageText': self.messageText,
            'isRead': self.isRead,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

    def to_dict(self):
        return {
            'id': self.id,
            'requestId': self.requestId,
            'customerId': self.customerId,
            'providerId': self.providerId,
            'amount': float(self.amount) if self.amount else None,
            'status': self.status,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

    # Relationships
    payment = db.relationship('Payment', backref='service_request', uselist=False)
    conversation = db.relationship('Conversation', backref='service_request', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customerId': self.customerId,
            'serviceId': self.serviceId,
            'requestType': self.requestType,
            'scheduledTime': self.scheduledTime.isoformat() if self.scheduledTime else None,
            'status': self.status,
            'completedAt': self.completedAt.isoformat() if self.completedAt else None,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

class Payment(db.Model):
    __tablename__ = 'Payments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requestId = db.Column(db.Integer, db.ForeignKey('ServiceRequests.id'), nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    providerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(Enum('pending', 'completed', 'failed', name='payment_status'), default='pending')
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class Review(db.Model):
    __tablename__ = 'Reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serviceId = db.Column(db.Integer, db.ForeignKey('Services.id'), nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class JobStat(db.Model):
    __tablename__ = 'JobStats'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    providerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False, unique=True)
    totalJobs = db.Column(db.Integer, default=0)
    totalEarnings = db.Column(db.Numeric(12, 2), default=0.0)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class Conversation(db.Model):
    __tablename__ = 'Conversations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requestId = db.Column(db.Integer, db.ForeignKey('ServiceRequests.id'), nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    providerId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # Relationships
    messages = db.relationship('Message', backref='conversation', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'requestId': self.requestId,
            'customerId': self.customerId,
            'providerId': self.providerId,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None,
            'updatedAt': self.updatedAt.isoformat() if self.updatedAt else None
        }

class Message(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conversationId = db.Column(db.Integer, db.ForeignKey('Conversations.id'), nullable=False)
    senderId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    messageText = db.Column(db.Text)
    isRead = db.Column(db.Boolean, default=False)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class AdminApproval(db.Model):
    __tablename__ = 'AdminApprovals'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adminId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    approvedBy = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class PasswordReset(db.Model):
    __tablename__ = 'PasswordResets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    resetToken = db.Column(db.String(255), nullable=False, unique=True)
    resetBy = db.Column(db.Integer, db.ForeignKey('Users.id'))
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())