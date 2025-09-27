import os
from dotenv import load_dotenv
from flask import Flask
from config import Config
from models import db, User

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    users = User.query.all()
    print("Users in the database:")
    for user in users:
        print(f"Email: {user.email}, Password Hash: {user.password_hash}")