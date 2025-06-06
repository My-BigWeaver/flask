from .default import DefaultConfig

class ProductionConfig(DefaultConfig):
    """Production configuration."""
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    
    # Ensure debug is off in production
    DEBUG = False
    
    # Production database
    DATABASE_URI = 'postgresql://user:pass@localhost/dbname'  # Override with environment variable
    
    # Production-specific settings
    PREFERRED_URL_SCHEME = 'https'