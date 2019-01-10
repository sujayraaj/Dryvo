import os


class Config(object):
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SESSION_TYPE = "filesystem"  # meanwhile, let's use filesystem session

    def update(self, newdata):
        for key, value in newdata.items():
            setattr(self, key, value)
