import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "2fwDQKF8bG15iof0XGETBL0HfSxeIGdP"

    MONGODB_SETTINGS = {'db'    : 'Project_Roboto',
                        'host'  : 'localhost',
                        'port'  :27017
    }
