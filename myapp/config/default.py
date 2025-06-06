import os

class DefaultConfig:
    """Default configuration for Flask application."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')  # Change in production!
    
    # Application settings
    DEBUG = False
    TESTING = False
    
    # Database settings
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
    
    # Session settings
    SESSION_COOKIE_NAME = 'myapp_session'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  # Set to True in production
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    
    # Static files
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'