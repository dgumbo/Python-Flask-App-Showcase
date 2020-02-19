from common.models.Base_Entity import BaseEntity,db

class Service(BaseEntity, db.Model):
     
    def __init__(self):
        BaseEntity(self)