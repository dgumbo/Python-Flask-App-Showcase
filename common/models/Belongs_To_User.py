from db_holder import db
from auth.models.User import User
from common.models.Base_Entity import BaseEntity

from sqlalchemy.ext.declarative import declarative_base, declared_attr

class BelongsToUser(BaseEntity): 

    # @declared_attr
    user = db.relationship(User, backref='owner', lazy='dynamic')    
 
    def __init__(self, user ):
        BaseEntity.__init__(self)
        self.user = user  