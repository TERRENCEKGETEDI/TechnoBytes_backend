-- Mock data for TechnoBytes Backend Database
-- PL/SQL INSERT statements

-- Users
INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440000', 'John Doe', 'john@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27123456789', 'Johannesburg, South Africa', 'https://example.com/avatar1.jpg', 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440001', 'Jane Smith', 'jane@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27987654321', 'Cape Town, South Africa', 'https://example.com/avatar2.jpg', 4.50, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440002', 'Bob Johnson', 'bob@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27112233445', 'Durban, South Africa', NULL, 0.00, FALSE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440003', 'Alice Brown', 'alice@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27556677889', 'Pretoria, South Africa', 'https://example.com/avatar3.jpg', 4.20, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440004', 'Charlie Wilson', 'charlie@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27334455667', 'Bloemfontein, South Africa', NULL, 3.80, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440005', 'Diana Prince', 'diana@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27778899001', 'Port Elizabeth, South Africa', 'https://example.com/avatar4.jpg', 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440006', 'Eve Garcia', 'eve@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27123409876', 'East London, South Africa', NULL, 4.70, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440007', 'Frank Miller', 'frank@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27543210987', 'Kimberley, South Africa', NULL, 0.00, FALSE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440008', 'Grace Lee', 'grace@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27654321098', 'Polokwane, South Africa', 'https://example.com/avatar5.jpg', 4.90, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440009', 'Henry Taylor', 'henry@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27876543210', 'Nelspruit, South Africa', NULL, 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440010', 'Ivy Martinez', 'ivy@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27109876543', 'Rustenburg, South Africa', NULL, 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440011', 'Jack Davis', 'jack@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27234567890', 'Upington, South Africa', 'https://example.com/avatar6.jpg', 4.30, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440012', 'Kara White', 'kara@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27345678901', 'George, South Africa', NULL, 0.00, FALSE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440013', 'Liam Harris', 'liam@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27456789012', 'Pietermaritzburg, South Africa', NULL, 3.90, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440014', 'Mia Clark', 'mia@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27567890123', 'Richards Bay, South Africa', 'https://example.com/avatar7.jpg', 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440015', 'Noah Lewis', 'noah@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27678901234', 'Vereeniging, South Africa', NULL, 4.60, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440006', 'Painting', 'fa-paint-brush', '#FF9FF3', 'Interior and exterior painting services for homes and businesses', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440007', 'IT Support', 'fa-desktop', '#A29BFE', 'Computer repair, software installation, and technical support', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440008', 'Pet Care', 'fa-paw', '#FD79A8', 'Pet sitting, walking, grooming, and veterinary assistance', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440009', 'Moving Services', 'fa-truck', '#00B894', 'Professional moving, packing, and transportation services', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
VALUES ('550e8400-e29b-41d4-a716-446655440016', 'Olivia Walker', 'olivia@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27789012345', 'Soweto, South Africa', NULL, 0.00, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440017', 'Parker Hall', 'parker@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27890123456', 'Centurion, South Africa', 'https://example.com/avatar8.jpg', 4.10, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440018', 'Quinn Young', 'quinn@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'customer', '+27901234567', 'Roodepoort, South Africa', NULL, 0.00, FALSE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440011', '660e8400-e29b-41d4-a716-446655440006', 'Interior Painting Services', 'Professional interior painting with premium quality paints.', 'Upington, South Africa', 120.00, 'hourly', '["https://example.com/painting1.jpg"]', 4.30, 7, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440013', '660e8400-e29b-41d4-a716-446655440007', 'Computer Repair & IT Support', 'Fix computers, install software, and provide tech support.', 'Pietermaritzburg, South Africa', 80.00, 'hourly', NULL, 3.90, 10, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440008', '550e8400-e29b-41d4-a716-446655440015', '660e8400-e29b-41d4-a716-446655440008', 'Pet Sitting & Walking', 'Reliable pet care services for dogs and cats.', 'Vereeniging, South Africa', 40.00, 'hourly', '["https://example.com/pet1.jpg"]', 4.60, 18, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440017', '660e8400-e29b-41d4-a716-446655440009', 'Moving & Packing Services', 'Full-service moving with packing and transportation.', 'Centurion, South Africa', 250.00, 'fixed', NULL, 4.10, 12, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440019', '660e8400-e29b-41d4-a716-446655440000', 'Emergency Plumbing', '24/7 emergency plumbing repairs and installations.', 'Midrand, South Africa', 180.00, 'hourly', '["https://example.com/plumbing2.jpg"]', 4.40, 9, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440005', '770e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440011', 'accepted', 'Paint my living room and hallway.', '\1'::date, 8, '+27109876543', 'ivy@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440006', '770e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440012', '550e8400-e29b-41d4-a716-446655440013', 'completed', 'My laptop is running slow, needs optimization.', '\1'::date, 2, '+27345678901', 'kara@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440007', '770e8400-e29b-41d4-a716-446655440008', '550e8400-e29b-41d4-a716-446655440014', '550e8400-e29b-41d4-a716-446655440015', 'pending', 'Walk my dog twice a day for a week.', '\1'::date, 14, '+27567890123', 'mia@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO feedback (id, service_request_id, customer_id, provider_id, rating, comment, is_public, created_at)
VALUES ('990e8400-e29b-41d4-a716-446655440002', '880e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440012', '550e8400-e29b-41d4-a716-446655440013', 4, 'Great job optimizing my laptop. It runs much faster now.', TRUE, CURRENT_TIMESTAMP);

INSERT INTO feedback (id, service_request_id, customer_id, provider_id, rating, comment, is_public, created_at)
VALUES ('990e8400-e29b-41d4-a716-446655440003', '880e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440018', '550e8400-e29b-41d4-a716-446655440019', 5, 'Quick and efficient plumbing service. Highly recommended!', TRUE, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440008', '770e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440016', '550e8400-e29b-41d4-a716-446655440017', 'accepted', 'Help me move to a new apartment next weekend.', '\1'::date, 6, '+27789012345', 'olivia@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440011', 'request', 'New Service Request', 'You have a new request for Interior Painting Services.', '{"service_id": "770e8400-e29b-41d4-a716-446655440006", "request_id": "880e8400-e29b-41d4-a716-446655440005"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440013', 'request', 'New Service Request', 'You have a new request for Computer Repair & IT Support.', '{"service_id": "770e8400-e29b-41d4-a716-446655440007", "request_id": "880e8400-e29b-41d4-a716-446655440006"}', TRUE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440015', 'request', 'New Service Request', 'You have a new request for Pet Sitting & Walking.', '{"service_id": "770e8400-e29b-41d4-a716-446655440008", "request_id": "880e8400-e29b-41d4-a716-446655440007"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440017', 'request', 'New Service Request', 'You have a new request for Moving & Packing Services.', '{"service_id": "770e8400-e29b-41d4-a716-446655440009", "request_id": "880e8400-e29b-41d4-a716-446655440008"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440019', 'request', 'New Service Request', 'You have a new request for Emergency Plumbing.', '{"service_id": "770e8400-e29b-41d4-a716-446655440010", "request_id": "880e8400-e29b-41d4-a716-446655440009"}', TRUE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440008', '550e8400-e29b-41d4-a716-446655440011', 'request', 'New Service Request', 'You have a new request for Lawn Care & Landscaping.', '{"service_id": "770e8400-e29b-41d4-a716-446655440011", "request_id": "880e8400-e29b-41d4-a716-446655440010"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440012', 'completion', 'Service Completed', 'Your computer repair service has been completed.', '{"request_id": "880e8400-e29b-41d4-a716-446655440006"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440018', 'completion', 'Service Completed', 'Your plumbing service has been completed.', '{"request_id": "880e8400-e29b-41d4-a716-446655440009"}', TRUE, CURRENT_TIMESTAMP);
VALUES ('880e8400-e29b-41d4-a716-446655440009', '770e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440018', '550e8400-e29b-41d4-a716-446655440019', 'completed', 'Bathroom sink is clogged and leaking.', '\1'::date, 1, '+27901234567', 'quinn@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440010', '770e8400-e29b-41d4-a716-446655440011', '550e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440011', 'pending', 'Mow the lawn and trim the hedges.', '\1'::date, 4, '+27123456789', 'john@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
VALUES ('770e8400-e29b-41d4-a716-446655440011', '550e8400-e29b-41d4-a716-446655440011', '660e8400-e29b-41d4-a716-446655440003', 'Lawn Care & Landscaping', 'Complete lawn maintenance and landscaping design.', 'Upington, South Africa', 90.00, 'hourly', NULL, 4.30, 14, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO users (id, name, email, password_hash, role, phone, location, avatar_url, rating, is_verified, is_active, created_at, updated_at)
VALUES ('550e8400-e29b-41d4-a716-446655440019', 'Riley King', 'riley@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6fMxzVLfO', 'provider', '+27102345678', 'Midrand, South Africa', NULL, 4.40, TRUE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Service Categories
INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440000', 'Plumbing', 'fa-wrench', '#FF6B6B', 'Professional plumbing services for homes and businesses', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440001', 'Electrical', 'fa-bolt', '#4ECDC4', 'Electrical installation, repair, and maintenance services', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440002', 'Cleaning', 'fa-broom', '#45B7D1', 'House cleaning, office cleaning, and deep cleaning services', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440003', 'Gardening', 'fa-leaf', '#96CEB4', 'Lawn care, landscaping, and garden maintenance', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440004', 'Tutoring', 'fa-graduation-cap', '#FFEAA7', 'Academic tutoring and educational support services', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_categories (id, name, icon, color, description, is_active, created_at, updated_at)
VALUES ('660e8400-e29b-41d4-a716-446655440005', 'Carpentry', 'fa-hammer', '#DDA0DD', 'Woodworking, furniture repair, and construction services', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Services
INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440001', '660e8400-e29b-41d4-a716-446655440000', 'Expert Plumbing Services', 'Professional plumber with 10 years experience. Fix leaks, install fixtures, and more.', 'Cape Town, South Africa', 150.00, 'hourly', '["https://example.com/plumbing1.jpg"]', 4.50, 12, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440003', '660e8400-e29b-41d4-a716-446655440001', 'Electrical Repairs & Installations', 'Licensed electrician specializing in residential and commercial electrical work.', 'Pretoria, South Africa', 200.00, 'hourly', '["https://example.com/electrical1.jpg", "https://example.com/electrical2.jpg"]', 4.20, 8, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440004', '660e8400-e29b-41d4-a716-446655440002', 'Deep Cleaning Services', 'Thorough cleaning of homes and offices. Eco-friendly products used.', 'Bloemfontein, South Africa', 80.00, 'fixed', NULL, 3.80, 15, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440006', '660e8400-e29b-41d4-a716-446655440003', 'Garden Maintenance', 'Lawn mowing, trimming, and general garden upkeep.', 'East London, South Africa', 100.00, 'hourly', '["https://example.com/garden1.jpg"]', 4.70, 20, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440008', '660e8400-e29b-41d4-a716-446655440004', 'Math Tutoring', 'Experienced math tutor for high school and university students.', 'Polokwane, South Africa', 50.00, 'hourly', NULL, 4.90, 25, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO services (id, provider_id, category_id, title, description, location, price, price_type, images, rating, review_count, is_active, created_at, updated_at)
VALUES ('770e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440003', '660e8400-e29b-41d4-a716-446655440005', 'Custom Carpentry', 'Handcrafted furniture and woodworking services.', 'Pretoria, South Africa', 300.00, 'fixed', '["https://example.com/carpentry1.jpg"]', 4.20, 5, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Service Requests
INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440000', '770e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440001', 'completed', 'Need help fixing a leaky faucet in the kitchen.', '\1'::date, 2, '+27123456789', 'john@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440001', '770e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440003', 'accepted', 'Light fixture in living room needs replacement.', '\1'::date, 3, '+27112233445', 'bob@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440002', '770e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440004', 'pending', 'Deep clean my 3-bedroom apartment.', '\1'::date, 4, '+27778899001', 'diana@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440003', '770e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440006', 'completed', 'Weekly garden maintenance for my yard.', '\1'::date, 6, '+27543210987', 'frank@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_requests (id, service_id, customer_id, provider_id, status, message, requested_date, estimated_duration, customer_phone, customer_email, created_at, updated_at)
VALUES ('880e8400-e29b-41d4-a716-446655440004', '770e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440008', 'accepted', 'Help with calculus homework for my son.', '\1'::date, 2, '+27876543210', 'henry@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Feedback
INSERT INTO feedback (id, service_request_id, customer_id, provider_id, rating, comment, is_public, created_at)
VALUES ('990e8400-e29b-41d4-a716-446655440000', '880e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440001', 5, 'Excellent service! Fixed the leak quickly and professionally.', TRUE, CURRENT_TIMESTAMP);

INSERT INTO feedback (id, service_request_id, customer_id, provider_id, rating, comment, is_public, created_at)
VALUES ('990e8400-e29b-41d4-a716-446655440001', '880e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440006', 4, 'Good job on the garden. Will hire again.', TRUE, CURRENT_TIMESTAMP);

-- Notifications
INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440000', '550e8400-e29b-41d4-a716-446655440000', 'request', 'New Service Request', 'You have a new request for Expert Plumbing Services.', '{"service_id": "770e8400-e29b-41d4-a716-446655440000", "request_id": "880e8400-e29b-41d4-a716-446655440000"}', FALSE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440001', 'acceptance', 'Request Accepted', 'Your request has been accepted.', '{"request_id": "880e8400-e29b-41d4-a716-446655440000"}', TRUE, CURRENT_TIMESTAMP);

INSERT INTO notifications (id, user_id, type, title, message, data, is_read, created_at)
VALUES ('aa0e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440003', 'request', 'New Service Request', 'You have a new request for Electrical Repairs & Installations.', '{"service_id": "770e8400-e29b-41d4-a716-446655440001", "request_id": "880e8400-e29b-41d4-a716-446655440001"}', FALSE, CURRENT_TIMESTAMP);

COMMIT;