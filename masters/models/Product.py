from common.models.Base_Entity import BaseEntity, db
from auth.models.User import User

class Product(BaseEntity, db.Model):
     
    name = db.Column(db.String(64), nullable=False)   
    description = db.Column(db.String(254) )   
    price = db.Column(db.Numeric(12, 6) )    
     
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )

    def __init__(self, user:User, name, description, price):
        BaseEntity.__init__(self) 

        self.owner_id = user.id  

        self.name = name 
        self.description = description 
        self.price = price

        # name description cost