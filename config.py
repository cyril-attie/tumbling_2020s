import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'e7f5623537dc02a528e7905b7646a73a3840857ada767d81f0bdfe56f0bf07f2'
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True