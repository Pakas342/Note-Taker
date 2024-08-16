import os

print(os.urandom(12))

class Config(object):
    TESTING = False
    
class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv("DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")
    
class TestEnvironConfig(Config):
    TESTING = True
    SECRET_KEY = os.getenv("TEST_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_TEST_DB_URI")
    
    