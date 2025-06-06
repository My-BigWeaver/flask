# Flask Application Template

This is a Flask application template with a clean, maintainable structure following best practices.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── config.py
├── requirements.txt
└── run.py
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file:
   ```bash
   touch .env
   # Add environment variables like:
   # FLASK_ENV=development
   # SECRET_KEY=your-secret-key
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Run tests:
   ```bash
   pytest
   ```

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## Development

- The application uses a factory pattern for initialization
- Configuration is handled through environment variables and the config.py file
- Tests are written using pytest