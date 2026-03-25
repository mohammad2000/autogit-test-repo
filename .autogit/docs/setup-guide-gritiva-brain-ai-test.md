# Setup Guide for Gritiva Brain AI Test

This guide provides step-by-step instructions to set up and configure the Gritiva Brain AI Test project, a FastAPI application designed for testing commit message generation.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before setting up the Gritiva Brain AI Test project, ensure you have the following prerequisites installed on your system:

1. **Python**: Version 3.8 or higher is recommended.
2. **pip**: The Python package installer.
3. **Git**: For version control and cloning the repository.

## Installation

To install the Gritiva Brain AI Test project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-url/gritiva-brain-ai-test.git
   cd gritiva-brain-ai-test
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The Gritiva Brain AI Test project uses environment variables for configuration. You can configure the application by creating a `.env` file in the root directory of the project.

### Environment Variables

Create a `.env.local` file to store your local environment variables. Here is an example configuration:

```plaintext
# .env.local
DATABASE_URL=sqlite:///./test.db  # Example database URL
SECRET_KEY=your_secret_key       # Secret key for JWT authentication
ALGORITHM=HS256                  # Algorithm used for JWT encoding
ACCESS_TOKEN_EXPIRE_MINUTES=30    # Token expiration time in minutes
```

### Configuration Options

| Variable Name                | Description                           | Default Value          |
|------------------------------|---------------------------------------|------------------------|
| `DATABASE_URL`               | URL of the database                   | `sqlite:///./test.db`   |
| `SECRET_KEY`                 | Secret key for JWT authentication     | Required               |
| `ALGORITHM`                  | Algorithm used for JWT encoding       | `HS256`                |
| `ACCESS_TOKEN_EXPIRE_MINUTES`| Token expiration time in minutes      | 30                     |

## Running the Application

To run the Gritiva Brain AI Test application, use the following command:

```bash
python api_routes.py
```

By default, the application will start on `http://127.0.0.1:8000`.

### Available Endpoints

- **POST /api/v1/login**: Authenticate user and return token.
- **POST /api/v1/logout**: Invalidate session token.
- **GET /api/v1/me**: Get current authenticated user.
- **GET /api/v1/health**: Application health check endpoint.

## Troubleshooting

If you encounter any issues during the setup or while running the application, consider the following troubleshooting steps:

1. **Check Environment Variables**: Ensure all required environment variables are set correctly in your `.env.local` file.

2. **Verify Dependencies**: Make sure all dependencies are installed. You can reinstall them using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Connection**: If you're using a database, ensure the `DATABASE_URL` is correct and the database server is running.

4. **Logs and Errors**: Check the console output for any error messages or logs that can provide more context about the issue.

5. **Consult Documentation**: Refer to the [API Documentation](api-documentation-autogit-test-repo) for detailed information on each endpoint and their expected behavior.

If you continue to experience issues, please consult the [Contributing Guide](contributing-guide-autogit-test-repo) or reach out to the support team for assistance.