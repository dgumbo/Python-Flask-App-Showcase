from common.models.Base_Entity import BaseEntity, db

class Client(BaseEntity, db.Model):
     
    def __init__(self):
        BaseEntity(self)