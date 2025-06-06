import pytest
from myapp import create_app
from myapp.config import TestingConfig

def test_config():
    """Test configuration loading."""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_testing_config():
    """Test testing configuration."""
    app = create_app(TestingConfig)
    assert app.config['TESTING']
    assert not app.config['DEBUG']
    assert app.config['DATABASE_URI'] == 'sqlite:///:memory:'

def test_development_config():
    """Test development configuration."""
    app = create_app()
    app.config.from_object('myapp.config.development.DevelopmentConfig')
    assert app.config['DEBUG']
    assert app.config['TEMPLATES_AUTO_RELOAD']
    assert app.config['DATABASE_URI'] == 'sqlite:///dev.db'

def test_production_config():
    """Test production configuration."""
    app = create_app()
    app.config.from_object('myapp.config.production.ProductionConfig')
    assert not app.config['DEBUG']
    assert app.config['SESSION_COOKIE_SECURE']
    assert app.config['PREFERRED_URL_SCHEME'] == 'https'