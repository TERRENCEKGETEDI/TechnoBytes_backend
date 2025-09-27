import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 604800))  # 7 days
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    HOME_AFFAIRS_API_BASE = os.getenv('HOME_AFFAIRS_API_BASE', 'https://api.example.com')
    PORT = int(os.getenv('PORT', 4000))
    REDIS_URL = os.getenv('REDIS_URL', 'memory://')