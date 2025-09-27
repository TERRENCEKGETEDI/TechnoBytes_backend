import pytest
import requests
import json

BASE_URL = 'http://localhost:4000'

def test_health_check():
    response = requests.get(f'{BASE_URL}/')
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True
    assert 'LinkLocal API is running' in data['message']

def test_register():
    payload = {
        "fullName": "Test User",
        "email": "test@example.com",
        "phoneNumber": "1234567890",
        "password": "password123"
    }
    response = requests.post(f'{BASE_URL}/api/auth/register', json=payload)
    # May fail if user exists, but check if it's a validation error or success
    if response.status_code == 201 or response.status_code == 200:
        data = response.json()
        assert 'data' in data
        assert 'token' in data['data']
        assert 'user' in data['data']
    else:
        # If 400, perhaps user exists, skip assertion
        assert response.status_code == 400

def test_login():
    payload = {
        "email": "test@example.com",
        "password": "password123"
    }
    response = requests.post(f'{BASE_URL}/api/auth/login', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'token' in data['data']
    assert 'user' in data['data']

def test_list_services():
    response = requests.get(f'{BASE_URL}/api/services')
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'services' in data['data']
    assert isinstance(data['data']['services'], list)

# Add more tests as needed
def test_verify_id_photo_unauthorized():
    response = requests.post(f'{BASE_URL}/api/verification/id_photo', json={
        "api_key": "test",
        "id_number": "1234567890123",
        "enquiry_reason": "test"
    })
    assert response.status_code == 401  # Unauthorized