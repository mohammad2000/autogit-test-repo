# API Documentation

## Overview

This document provides comprehensive RESTful API documentation for Gritiva Brain AI Test, a FastAPI application designed to test commit message generation. The API includes endpoints for authentication, user management, and health checks.

## Authentication

Gritiva Brain AI Test uses JSON Web Tokens (JWT) for authentication. Each request that requires authentication must include the `Authorization` header with a valid JWT token.

### Base URL

The base URL for all API endpoints is:

```
https://api.gritivabrain.com
```

## Endpoints

### User Authentication

#### POST /api/v1/login

Authenticate a user and return a JWT token.

**Request Body**

```json
{
  "username": "string",
  "password": "string"
}
```

**Response**

- **200 OK**
  
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

- **401 Unauthorized**
  
  ```json
  {
    "detail": "Incorrect username or password"
  }
  ```

#### POST /api/v1/logout

Invalidate the session token.

**Request Headers**

```http
Authorization: Bearer <token>
```

**Response**

- **200 OK**
  
  ```json
  {
    "message": "Successfully logged out"
  }
  ```

### User Management

#### GET /api/v1/me

Get details of the current authenticated user.

**Request Headers**

```http
Authorization: Bearer <token>
```

**Response**

- **200 OK**
  
  ```json
  {
    "username": "string",
    "email": "string"
  }
  ```

### Application Health

#### GET /api/v1/health

Check the application's health status.

**Response**

- **200 OK**
  
  ```json
  {
    "status": "ok"
  }
  ```

## Error Codes

| Status Code | Description                |
|-------------|----------------------------|
| 400         | Bad Request                |
| 401         | Unauthorized               |
| 403         | Forbidden                  |
| 404         | Not Found                  |
| 500         | Internal Server Error      |

## Rate Limits

The API has rate limits to prevent abuse. The current rate limit is set to **100 requests per minute** per user.

## Security

- **JWT Authentication**: All endpoints that require authentication use JWT for secure access.
- **HTTPS**: Ensure all API calls are made over HTTPS to protect data in transit.

## Conclusion

This API documentation provides a comprehensive guide on how to interact with the Gritiva Brain AI Test application. For more detailed information, refer to the [Architecture Guide](architecture-guide-autogit-test-repo) and [Contributing Guide](contributing-guide-autogit-test-repo).