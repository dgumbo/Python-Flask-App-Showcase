from common.models.Base_Entity import BaseEntity, db 
from auth.models.User import User

class Client(BaseEntity, db.Model):
    __tablename__ = 'clients'

    name = db.Column( db.String, nullable=False )  
    phone = db.Column( db.String, nullable=False )  
    address_1 = db.Column( db.String, nullable=False )  
    address_2 = db.Column( db.String )  
    city = db.Column( db.String, nullable=False )  
    post_code = db.Column( db.String, nullable=False )  
     
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )
     
    def __init__(self, user:User, name, phone, address_1, address_2, city, post_code):
        BaseEntity.__init__(self)

        self.owner_id = user.id  

        self.name = name 
        self.phone = phone 
        self.address_1 = address_1 
        self.address_2 = address_2 
        self.city = city 
        self.post_code = post_code


        # name phone address_1 address_2 city post_code