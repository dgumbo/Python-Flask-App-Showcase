from common.models.Base_Entity import BaseEntity, db
from auth.models.User import User

class PaymentDetail(BaseEntity, db.Model):
      
    acc_name = db.Column(db.String(64), nullable=False)   
    bank_name = db.Column(db.String(64), nullable=False)   
    sort_code = db.Column(db.String(6), nullable=False)   
    acc_number = db.Column(db.String(8), nullable=False)  
     
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )

    def __init__(self, user:User, acc_name, bank_name, sort_code, acc_number):
        BaseEntity.__init__(self) 

        self.owner_id = user.id  
        
        self. acc_name = acc_name
        self.bank_name = bank_name
        self.sort_code = sort_code
        self.acc_number = acc_number

