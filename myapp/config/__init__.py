from .default import DefaultConfig
from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig

# Dictionary to map environment names to config classes
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(environment=None):
    """Helper function to get the config class based on environment."""
    if environment is None:
        environment = 'default'
    return config.get(environment, config['default'])