<!-- Revision 2: Fixed placeholder URLs, consolidated Installation and Quick Start sections, and added a Troubleshooting section -->

# Gritiva Brain AI Test

## Overview

Gritiva Brain AI Test is a simple FastAPI application designed for testing commit message generation. The project leverages FastAPI's capabilities to provide efficient and scalable RESTful APIs, with JWT (JSON Web Token) authentication for secure access.

## Features

- **Commit Message Generation**: API endpoints for generating AI-powered commit messages.
- **Authentication & Authorization**: Secure user login and logout using JWT tokens.
- **User Management**: Retrieve current authenticated user details.
- **Health Check**: Endpoint to monitor application health and status.
- **Dependency Injection**: Utilizes FastAPI's dependency injection pattern for cleaner code.
- **Environment Configuration**: Managed via environment variables, ensuring flexibility and security.

## Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/gritiva-brain-ai-test.git
   cd gritiva-brain-ai-test
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env.local` file in the root directory with the following content:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///./test.db  # Adjust for your database setup if needed
   ```

4. **Run the Application**:
   ```bash
   uvicorn api_routes:app --reload
   ```

5. **Access the API**:
   - Open your browser or use a tool like Postman to access `http://127.0.0.1:8000/docs` for interactive API documentation.
   - Use the `/api/v1/login` endpoint to authenticate and obtain a token.

## Installation

To install the project dependencies, follow these steps:

1. **Ensure Python & pip are Installed**:
   Make sure you have Python 3.7+ and pip installed on your system.

2. **Install Dependencies**:
   Navigate to the project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Authentication

- **Login**:
  Send a POST request to `/api/v1/login` with JSON body containing `username` and `password`.
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
  Response will include an access token.

- **Logout**:
  Send a POST request to `/api/v1/logout` with the authorization header set to your JWT token.
  ```bash
  curl -X POST http://127.0.0.1:8000/api/v1/logout \
  -H "Authorization: Bearer your_access_token"
  ```

### User Management

- **Get Current User**:
  Send a GET request to `/api/v1/me` with the authorization header set to your JWT token.
  ```bash
  curl http://127.0.0.1:8000/api/v1/me \
  -H "Authorization: Bearer your_access_token"
  ```

### Health Check

- **Check Application Health**:
  Send a GET request to `/api/v1/health`.
  ```bash
  curl http://127.0.0.1:8000/api/v1/health
  ```

## Configuration

Configuration is managed via environment variables, specifically through `.env.local` and `.env.test` files.

- **SECRET_KEY**: A secret key for JWT token encoding.
- **DATABASE_URL**: URL for the database connection (e.g., `sqlite:///./test.db`).

## API

For detailed API documentation, please refer to the [API Documentation](https://github.com/your-repo/gritiva-brain-ai-test/blob/main/docs/api-documentation.md).

## Troubleshooting

If you encounter any issues during setup or usage, consider the following troubleshooting steps:

1. **Check Environment Variables**: Ensure all required environment variables are set correctly in your `.env.local` file.
2. **Verify Dependencies**: Make sure all dependencies are installed by running `pip install -r requirements.txt`.
3. **Review Logs**: Check the application logs for any error messages that can help diagnose issues.
4. **Check Network Connections**: Ensure there are no network connectivity issues preventing access to the API endpoints.

## Contributing

To contribute to this project, follow the guidelines in the [Contributing Guide](https://github.com/your-repo/gritiva-brain-ai-test/blob/main/docs/contributing-guide.md).

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

---

[!NOTE] This documentation provides a comprehensive overview of Gritiva Brain AI Test. For detailed technical insights and further customization options, please refer to the [Architecture Guide](https://github.com/your-repo/gritiva-brain-ai-test/blob/main/docs/architecture-guide.md) and [Setup Guide](https://github.com/your-repo/gritiva-brain-ai-test/blob/main/docs/setup-guide.md).