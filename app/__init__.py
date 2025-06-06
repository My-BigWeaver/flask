from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app import routes
    app.register_blueprint(routes.main)

    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200

    return app