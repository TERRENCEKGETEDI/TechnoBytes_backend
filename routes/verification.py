from flask import Blueprint, request, jsonify, current_app
import requests
from flask_jwt_extended import jwt_required

verification_bp = Blueprint('verification', __name__)

@verification_bp.route('/id_photo', methods=['POST'])
@jwt_required()  # Require authentication
def verify_id_photo():
    data = request.get_json()
    api_key = data.get('api_key')
    id_number = data.get('id_number')
    enquiry_reason = data.get('enquiry_reason')

    if not all([api_key, id_number, enquiry_reason]):
        return jsonify({'success': False, 'error': 'Missing required fields: api_key, id_number, enquiry_reason'}), 400

    external_url = current_app.config['HOME_AFFAIRS_API_BASE'] + '/home_affairs_id_photo'

    try:
        response = requests.post(external_url, data={
            'api_key': api_key,
            'id_number': id_number,
            'enquiry_reason': enquiry_reason
        })
        response.raise_for_status()
        result = response.json()
        return jsonify({
            'success': True,
            'data': result,
            'message': 'ID verification successful'
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'error': str(e)}), 500