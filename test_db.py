from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    try:
        db.create_all()
        print("Database connection successful. Tables created.")
    except Exception as e:
        print(f"Database connection failed: {e}")