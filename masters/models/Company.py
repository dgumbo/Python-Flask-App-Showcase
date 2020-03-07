from common.models.Base_Entity import BaseEntity, db
from auth.models.User import User

class Company(BaseEntity, db.Model): 
      
    name = db.Column(db.String(64), nullable=False)   
    contact_person = db.Column(db.String(64) )   
    email = db.Column(db.String(50) )   
    phone = db.Column(db.String(25), nullable=False)  
    address_ln_1 = db.Column(db.String(100), nullable=False)  
    address_ln_2 = db.Column(db.String(100) )  
    city = db.Column(db.String(50), nullable=False)  
    postal_code = db.Column(db.String(15) )   
     
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )
    

    def __init__(self, user:User, name, contact_person, email, phone, address_ln_1, address_ln_2, city, postal_code):
        BaseEntity.__init__(self) 

        self.owner_id = user.id  
        
        self.trading_name=trading_name
        self.contact_person=contact_person
        self.email=email
        self.phone=phone
        self.address_ln_1=address_ln_1
        self.address_ln_2=address_ln_2
        self.city=city
        self.postal_code=postal_code

        