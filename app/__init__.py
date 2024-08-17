from config import DevelopmentConfig, TestEnvironConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize an instance of the SQAlchemy object
db = SQLAlchemy()
migrate = Migrate()

# List of valid config classes
VALID_CONFIG_CLASSES = {
    'DevelopmentConfig': DevelopmentConfig,
    'TestEnvironConfig': TestEnvironConfig,
}

def create_app(config_name="DevelopmentConfig"):
    # Checking if the given config is valid, and initializing a flask app
    if config_name not in VALID_CONFIG_CLASSES:
        raise ValueError(f"This config name {config_name} isn't part of the valid config classes!")
    
    config_class = VALID_CONFIG_CLASSES[config_name]
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #connecting the created SQLAchemy object to the flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    from main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app