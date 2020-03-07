from common.models.Base_Entity import BaseEntity,db
from auth.models.User import User

class Service(BaseEntity, db.Model):
     
    name = db.Column(db.String(64), nullable=False)   
    description = db.Column(db.String(254) )   
    charge = db.Column(db.Float )    
     
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )

    def __init__(self, user:User, name, description, charge):
        BaseEntity.__init__(self) 

        self.owner_id = user.id  

        self.name = name 
        self.description = description 
        self.charge = charge

        # name description cost