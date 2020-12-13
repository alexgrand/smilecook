class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://smilecook:97310852virus@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config fo JWT
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
