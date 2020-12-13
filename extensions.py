from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# JWT manager
from flask_jwt_extended import JWTManager
jwt = JWTManager()
