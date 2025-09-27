# Service Marketplace - Backend Starter

This repository contains a starter backend using Node.js, Express, Sequelize and PostgreSQL for the Service Marketplace app.

## Quick start
1. Copy `.env.example` to `.env` and fill values.
2. `npm install`
3. Ensure your Postgres database exists (e.g. `createdb service_marketplace`).
4. `npm run dev` (requires nodemon) or `npm start`.

## Notes
- This starter uses `sequelize.sync({ alter: true })` for dev convenience. In production use migrations.
- Payment handling here is mocked by creating a `Payment` record. Integrate a real gateway (Stripe/Paystack) for real flows.
- Socket.IO is included for real-time messaging.