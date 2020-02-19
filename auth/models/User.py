from common.models.Base_Entity import BaseEntity 
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

from db_holder import db, loginManager

bcrypt = Bcrypt()

class User(BaseEntity, db.Model, UserMixin): 
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, nullable=False, index=True) 
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)  
    password_hash = db.Column(db.String(128), nullable=False)  
    
    def __init__(self, username, email, password):
        BaseEntity.__init__(self)
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
