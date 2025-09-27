from flask import Blueprint, jsonify
from models import ServiceCategory

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('', methods=['GET'])
def get_categories():
    categories = ServiceCategory.query.filter_by(is_active=True).all()
    return jsonify({
        'success': True,
        'data': [cat.to_dict() for cat in categories]
    })