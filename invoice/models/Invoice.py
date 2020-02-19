from common.models.Base_Entity import BaseEntity, db

class Invoice(BaseEntity, db.Model):
     
    def __init__(self):
        BaseEntity(self)