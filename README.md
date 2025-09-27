# TechnoBytes Backend - Service Marketplace API

This repository contains the backend API for the Service Marketplace app, built with Python Flask, SQLAlchemy, and PostgreSQL.

## Features
- User authentication and authorization (JWT)
- Service listings and requests
- Real-time messaging with Socket.IO
- Payment processing (mocked)
- ID verification integration

## Local Development
1. Copy `.env.example` to `.env` and fill in the required values.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. The API will be available at `http://localhost:4000`

## API Documentation
See `API.md` for detailed endpoint documentation.

## Testing
Run tests with: `python -m pytest`

## Deployment on Render
1. Push this repository to GitHub.
2. Connect your GitHub repo to Render.
3. Create a new Web Service from the `render.yaml` configuration.
4. Set the following environment variables in Render:
   - `JWT_SECRET_KEY`: A secure random string
   - `HOME_AFFAIRS_API_BASE`: Base URL for the Home Affairs API
5. The database will be automatically provisioned by Render.

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string (provided by Render)
- `JWT_SECRET_KEY`: Secret key for JWT tokens
- `JWT_ACCESS_TOKEN_EXPIRES`: Token expiration time (default 7 days)
- `FLASK_ENV`: Environment (development/production)
- `HOME_AFFAIRS_API_BASE`: Base URL for external ID verification API