from config import DevelopmentConfig, TestEnvironConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor

# Initialize an instance of the SQAlchemy object
db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)


# List of valid config classes
VALID_CONFIG_CLASSES = {
    'DevelopmentConfig': DevelopmentConfig,
    'TestEnvironConfig': TestEnvironConfig,
}

def create_app(config_name="TestEnvironConfig"):
    # Checking if the given config is valid, and initializing a flask app
    if config_name not in VALID_CONFIG_CLASSES:
        raise ValueError(f"This config name {config_name} isn't part of the valid config classes!")
    
    config_class = VALID_CONFIG_CLASSES[config_name]
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #connecting the created SQLAchemy object to the flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Initialize the bootstap instance
    bootstrap = Bootstrap5(app) 
    
    # Initialize an instance of the CKEditor object
    ckeditor = CKEditor(app)
    
    # Register the created and linked blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app