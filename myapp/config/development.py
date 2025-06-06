from .default import DefaultConfig

class DevelopmentConfig(DefaultConfig):
    """Development configuration."""
    DEBUG = True
    
    # Development-specific settings
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True
    
    # Development database
    DATABASE_URI = 'sqlite:///dev.db'