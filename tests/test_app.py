import pytest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True

@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to the Flask API'}