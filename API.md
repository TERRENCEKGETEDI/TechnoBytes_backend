# Service Marketplace API Documentation

This document outlines the API endpoints and Socket.IO events for the Service Marketplace backend.

## Authentication

### Register
- **Endpoint**: `POST /api/auth/register`
- **Body**:
  ```json
  {
    "fullName": "string",
    "email": "string",
    "phoneNumber": "string",
    "password": "string",
    "role": "customer|provider|admin|master" // optional, defaults to customer
  }
  ```
- **Response**:
  ```json
  {
    "token": "jwt_token",
    "user": {
      "id": 1,
      "fullName": "string",
      "email": "string",
      "role": "string"
    }
  }
  ```

### Login
- **Endpoint**: `POST /api/auth/login`
- **Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**: Same as register

## Services

### Create Service (Provider Only)
- **Endpoint**: `POST /api/services`
- **Headers**: `Authorization: Bearer <token>`
- **Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "category": "string",
    "price": "decimal",
    "location": "string",
    "imageUrl": "string"
  }
  ```

### List Services
- **Endpoint**: `GET /api/services`
- **Query Params**: `category`, `location`, `q` (search in name)
- **Response**: Array of services with provider info

## Requests

### Create Request (Customer)
- **Endpoint**: `POST /api/requests`
- **Headers**: `Authorization: Bearer <token>`
- **Body**:
  ```json
  {
    "serviceId": 1,
    "requestType": "urgent|scheduled",
    "scheduledTime": "datetime" // optional
  }
  ```

### Accept Request (Provider)
- **Endpoint**: `POST /api/requests/:id/accept`
- **Headers**: `Authorization: Bearer <token>`

### Complete Request (Provider)
- **Endpoint**: `POST /api/requests/:id/complete`
- **Headers**: `Authorization: Bearer <token>`
- **Response**: Updated request and payment record

## Messages

### Create/Get Conversation
- **Endpoint**: `POST /api/messages/conversation`
- **Headers**: `Authorization: Bearer <token>`
- **Body**:
  ```json
  {
    "requestId": 1,
    "customerId": 1,
    "providerId": 1
  }
  ```

### Send Message
- **Endpoint**: `POST /api/messages/:conversationId/message`
- **Headers**: `Authorization: Bearer <token>`
- **Body**:
  ```json
  {
    "messageText": "string"
  }
  ```

## Socket.IO Events

### Connection
- **Auth**: Send token in `socket.handshake.auth.token`
- **Auto Join**: `user:${userId}` room

### Send Message
- **Event**: `send_message`
- **Payload**:
  ```json
  {
    "conversationId": 1,
    "messageText": "string"
  }
  ```
- **Emits**: `message` to `conversation:${conversationId}` room

### Receive Message
- **Event**: `message`
- **Payload**: Message object

## Frontend Expectations

### Joining Rooms
- On connection, frontend is auto-joined to `user:${userId}`
- For conversations, frontend should join `conversation:${conversationId}` when viewing a conversation
- Use `socket.join('conversation:' + conversationId)` after authenticating

### Real-time Updates
- Listen for `message` events on conversation rooms
- Update UI immediately when receiving messages

### Authentication
- Include JWT token in all API requests via Authorization header
- For Socket.IO, pass token in handshake auth