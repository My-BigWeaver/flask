from flask import Flask
from flask.config import Config
import os

def create_app(test_config=None):
    # Create Flask app instance
    app = Flask(__name__, instance_relative_config=True)
    
    # Load default configuration
    app.config.from_object('myapp.config.default.DefaultConfig')
    
    # Load environment specific configuration
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.update(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize extensions
    # db.init_app(app)
    
    # Register blueprints
    # from .views import main
    # app.register_blueprint(main.bp)
    
    return app