import os

class Config(object):
    # Used as signature key to ensure file cannot be hacked
    SECRET_KY = os.environ.get("SECRET_KEY") or "secret_string"