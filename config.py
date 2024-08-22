from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    TESTING = False
    
class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv("DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")
    
class TestEnvironConfig(Config):
    TESTING = False
    SECRET_KEY = os.environ["TEST_SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    
    