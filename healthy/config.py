""" Flask Configuration """
import os
from os import environ, path
from dotenv import load_dotenv, dotenv_values


basedir = path.abspath(path.dirname(__file__))
dotenv_values(path.join(basedir, '.env'))


class BaseConfig(object):
    """ Base/Core Configuration """
    DEBUG = False
    TESTING = False
    MONGO_URI = environ.get('MONGO_URI')
    SECRET_KEY = environ.get('SECRET_KEY')


class DevConfig(BaseConfig):
    """ Development Configuration """
    FLASK_ENV = 'development'
    DEBUG = True
    print("Dev Config Set")


class TestConfig(BaseConfig):
    """ Testing Configuration """
    FLASK_ENV = 'testing'
    TESTING = True
    DEBUG = True
    print("Test Config Set")


class ProdConfig(BaseConfig):
    """ Final/Production Configuration """
    FLASK_ENV = 'production'
    DEBUG = False
    print("Prod Config Set")


config_sel = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
    'default': DevConfig,
}
