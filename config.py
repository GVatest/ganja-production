import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_favourite_secret_key'

    # databases
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # admin
    FLASK_ADMIN_SWATCH = 'cerulean'

    # content path
    PATH_TO_CONTENT = 'app/static/content'

    # mail
    EMAIL_PASSWORD = 'qkwuzjuaqatisshb'
    EMAIL_SENDER = 'vasyaganzha@gmail.com'
    EMAIL_RECEIVER = 'ganjatriller@gmail.com'

    # instagram
    INST_USERNAME = '#'
    INST_PASSWORD = '#'
