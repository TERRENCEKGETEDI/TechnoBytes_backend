import os
from dotenv import load_dotenv
from flask import Flask
from config import Config
from models import db, User, ServiceCategory, Service, ServiceRequest, Feedback, Notification
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    # Create all tables
    db.create_all()
    print("Tables created successfully!")

    # Mock data
    users_data = [
        {'id': '550e8400-e29b-41d4-a716-446655440000', 'name': 'John Doe', 'email': 'john@example.com', 'role': 'customer', 'phone': '+27123456789', 'location': 'Johannesburg, South Africa', 'avatar_url': 'https://example.com/avatar1.jpg', 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440001', 'name': 'Jane Smith', 'email': 'jane@example.com', 'role': 'provider', 'phone': '+27987654321', 'location': 'Cape Town, South Africa', 'avatar_url': 'https://example.com/avatar2.jpg', 'rating': 4.50, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440002', 'name': 'Bob Johnson', 'email': 'bob@example.com', 'role': 'customer', 'phone': '+27112233445', 'location': 'Durban, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': False, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440003', 'name': 'Alice Brown', 'email': 'alice@example.com', 'role': 'provider', 'phone': '+27556677889', 'location': 'Pretoria, South Africa', 'avatar_url': 'https://example.com/avatar3.jpg', 'rating': 4.20, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440004', 'name': 'Charlie Wilson', 'email': 'charlie@example.com', 'role': 'provider', 'phone': '+27334455667', 'location': 'Bloemfontein, South Africa', 'avatar_url': None, 'rating': 3.80, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440005', 'name': 'Diana Prince', 'email': 'diana@example.com', 'role': 'customer', 'phone': '+27778899001', 'location': 'Port Elizabeth, South Africa', 'avatar_url': 'https://example.com/avatar4.jpg', 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440006', 'name': 'Eve Garcia', 'email': 'eve@example.com', 'role': 'provider', 'phone': '+27123409876', 'location': 'East London, South Africa', 'avatar_url': None, 'rating': 4.70, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440007', 'name': 'Frank Miller', 'email': 'frank@example.com', 'role': 'customer', 'phone': '+27543210987', 'location': 'Kimberley, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': False, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440008', 'name': 'Grace Lee', 'email': 'grace@example.com', 'role': 'provider', 'phone': '+27654321098', 'location': 'Polokwane, South Africa', 'avatar_url': 'https://example.com/avatar5.jpg', 'rating': 4.90, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440009', 'name': 'Henry Taylor', 'email': 'henry@example.com', 'role': 'customer', 'phone': '+27876543210', 'location': 'Nelspruit, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440010', 'name': 'Ivy Martinez', 'email': 'ivy@example.com', 'role': 'customer', 'phone': '+27109876543', 'location': 'Rustenburg, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440011', 'name': 'Jack Davis', 'email': 'jack@example.com', 'role': 'provider', 'phone': '+27234567890', 'location': 'Upington, South Africa', 'avatar_url': 'https://example.com/avatar6.jpg', 'rating': 4.30, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440012', 'name': 'Kara White', 'email': 'kara@example.com', 'role': 'customer', 'phone': '+27345678901', 'location': 'George, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': False, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440013', 'name': 'Liam Harris', 'email': 'liam@example.com', 'role': 'provider', 'phone': '+27456789012', 'location': 'Pietermaritzburg, South Africa', 'avatar_url': None, 'rating': 3.90, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440014', 'name': 'Mia Clark', 'email': 'mia@example.com', 'role': 'customer', 'phone': '+27567890123', 'location': 'Richards Bay, South Africa', 'avatar_url': 'https://example.com/avatar7.jpg', 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440015', 'name': 'Noah Lewis', 'email': 'noah@example.com', 'role': 'provider', 'phone': '+27678901234', 'location': 'Vereeniging, South Africa', 'avatar_url': None, 'rating': 4.60, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440016', 'name': 'Olivia Walker', 'email': 'olivia@example.com', 'role': 'customer', 'phone': '+27789012345', 'location': 'Soweto, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440017', 'name': 'Parker Hall', 'email': 'parker@example.com', 'role': 'provider', 'phone': '+27890123456', 'location': 'Centurion, South Africa', 'avatar_url': 'https://example.com/avatar8.jpg', 'rating': 4.10, 'is_verified': True, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440018', 'name': 'Quinn Young', 'email': 'quinn@example.com', 'role': 'customer', 'phone': '+27901234567', 'location': 'Roodepoort, South Africa', 'avatar_url': None, 'rating': 0.00, 'is_verified': False, 'is_active': True},
        {'id': '550e8400-e29b-41d4-a716-446655440019', 'name': 'Riley King', 'email': 'riley@example.com', 'role': 'provider', 'phone': '+27102345678', 'location': 'Midrand, South Africa', 'avatar_url': None, 'rating': 4.40, 'is_verified': True, 'is_active': True},
    ]

    for user_data in users_data:
        user = User(**user_data)
        user.set_password('password')  # Set a default password
        db.session.add(user)

    categories_data = [
        {'id': '660e8400-e29b-41d4-a716-446655440000', 'name': 'Plumbing', 'icon': 'fa-wrench', 'color': '#FF6B6B', 'description': 'Professional plumbing services for homes and businesses', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440001', 'name': 'Electrical', 'icon': 'fa-bolt', 'color': '#4ECDC4', 'description': 'Electrical installation, repair, and maintenance services', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440002', 'name': 'Cleaning', 'icon': 'fa-broom', 'color': '#45B7D1', 'description': 'House cleaning, office cleaning, and deep cleaning services', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440003', 'name': 'Gardening', 'icon': 'fa-leaf', 'color': '#96CEB4', 'description': 'Lawn care, landscaping, and garden maintenance', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440004', 'name': 'Tutoring', 'icon': 'fa-graduation-cap', 'color': '#FFEAA7', 'description': 'Academic tutoring and educational support services', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440005', 'name': 'Carpentry', 'icon': 'fa-hammer', 'color': '#DDA0DD', 'description': 'Woodworking, furniture repair, and construction services', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440006', 'name': 'Painting', 'icon': 'fa-paint-brush', 'color': '#FF9FF3', 'description': 'Interior and exterior painting services for homes and businesses', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440007', 'name': 'IT Support', 'icon': 'fa-desktop', 'color': '#A29BFE', 'description': 'Computer repair, software installation, and technical support', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440008', 'name': 'Pet Care', 'icon': 'fa-paw', 'color': '#FD79A8', 'description': 'Pet sitting, walking, grooming, and veterinary assistance', 'is_active': True},
        {'id': '660e8400-e29b-41d4-a716-446655440009', 'name': 'Moving Services', 'icon': 'fa-truck', 'color': '#00B894', 'description': 'Professional moving, packing, and transportation services', 'is_active': True},
    ]

    for cat_data in categories_data:
        cat = ServiceCategory(**cat_data)
        db.session.add(cat)

    # Commit users and categories first
    db.session.commit()
    print("Users and categories added successfully!")

    # Add services, requests, etc. similarly
    # For brevity, I'll add a few services
    services_data = [
        {'id': '770e8400-e29b-41d4-a716-446655440000', 'provider_id': '550e8400-e29b-41d4-a716-446655440001', 'category_id': '660e8400-e29b-41d4-a716-446655440000', 'title': 'Expert Plumbing Services', 'description': 'Professional plumber with 10 years experience. Fix leaks, install fixtures, and more.', 'location': 'Cape Town, South Africa', 'price': 150.00, 'price_type': 'hourly', 'images': ['https://example.com/plumbing1.jpg'], 'rating': 4.50, 'review_count': 12, 'is_active': True},
        {'id': '770e8400-e29b-41d4-a716-446655440001', 'provider_id': '550e8400-e29b-41d4-a716-446655440003', 'category_id': '660e8400-e29b-41d4-a716-446655440001', 'title': 'Electrical Repairs & Installations', 'description': 'Licensed electrician specializing in residential and commercial electrical work.', 'location': 'Pretoria, South Africa', 'price': 200.00, 'price_type': 'hourly', 'images': ['https://example.com/electrical1.jpg', 'https://example.com/electrical2.jpg'], 'rating': 4.20, 'review_count': 8, 'is_active': True},
        {'id': '770e8400-e29b-41d4-a716-446655440002', 'provider_id': '550e8400-e29b-41d4-a716-446655440004', 'category_id': '660e8400-e29b-41d4-a716-446655440002', 'title': 'Deep Cleaning Services', 'description': 'Thorough cleaning of homes and offices. Eco-friendly products used.', 'location': 'Bloemfontein, South Africa', 'price': 80.00, 'price_type': 'fixed', 'images': None, 'rating': 3.80, 'review_count': 15, 'is_active': True},
    ]

    for serv_data in services_data:
        serv = Service(**serv_data)
        db.session.add(serv)

    db.session.commit()
    print("Services added successfully!")

    # Add service requests
    requests_data = [
        {'id': '880e8400-e29b-41d4-a716-446655440000', 'service_id': '770e8400-e29b-41d4-a716-446655440000', 'customer_id': '550e8400-e29b-41d4-a716-446655440000', 'provider_id': '550e8400-e29b-41d4-a716-446655440001', 'status': 'completed', 'message': 'Need help fixing a leaky faucet in the kitchen.', 'requested_date': datetime(2023, 10, 15).date(), 'estimated_duration': 2, 'customer_phone': '+27123456789', 'customer_email': 'john@example.com'},
        {'id': '880e8400-e29b-41d4-a716-446655440001', 'service_id': '770e8400-e29b-41d4-a716-446655440001', 'customer_id': '550e8400-e29b-41d4-a716-446655440002', 'provider_id': '550e8400-e29b-41d4-a716-446655440003', 'status': 'accepted', 'message': 'Light fixture in living room needs replacement.', 'requested_date': datetime(2023, 10, 20).date(), 'estimated_duration': 3, 'customer_phone': '+27112233445', 'customer_email': 'bob@example.com'},
    ]

    for req_data in requests_data:
        req = ServiceRequest(**req_data)
        db.session.add(req)

    db.session.commit()
    print("Service requests added successfully!")

    # Add feedback
    feedback_data = [
        {'id': '990e8400-e29b-41d4-a716-446655440000', 'service_request_id': '880e8400-e29b-41d4-a716-446655440000', 'customer_id': '550e8400-e29b-41d4-a716-446655440000', 'provider_id': '550e8400-e29b-41d4-a716-446655440001', 'rating': 5, 'comment': 'Excellent service! Fixed the leak quickly and professionally.', 'is_public': True},
    ]

    for fb_data in feedback_data:
        fb = Feedback(**fb_data)
        db.session.add(fb)

    db.session.commit()
    print("Feedback added successfully!")

    # Add notifications
    notifications_data = [
        {'id': 'aa0e8400-e29b-41d4-a716-446655440000', 'user_id': '550e8400-e29b-41d4-a716-446655440000', 'type': 'request', 'title': 'New Service Request', 'message': 'You have a new request for Expert Plumbing Services.', 'data': {'service_id': '770e8400-e29b-41d4-a716-446655440000', 'request_id': '880e8400-e29b-41d4-a716-446655440000'}, 'is_read': False},
    ]

    for notif_data in notifications_data:
        notif = Notification(**notif_data)
        db.session.add(notif)

    db.session.commit()
    print("Notifications added successfully!")

    print("Mock data uploaded successfully!")