import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""
    SECRET_KEY='dev',
    DATABASE=':memory:'


class TestingConfig(Config):
    """Testing configuration"""


    TESTING = True