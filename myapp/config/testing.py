from .default import DefaultConfig

class TestingConfig(DefaultConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = False
    
    # Use in-memory database for testing
    DATABASE_URI = 'sqlite:///:memory:'
    
    # Test-specific settings
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in tests
    SERVER_NAME = 'localhost'