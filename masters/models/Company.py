from common.models.Base_Entity import BaseEntity, db

class Company(BaseEntity, db.Model):
     
    def __init__(self):
        BaseEntity(self)

        
      
    acc_name = db.Column(db.String(64), nullable=False)   
    bank_name = db.Column(db.String(64), nullable=False)   
    sort_code = db.Column(db.String(6), nullable=False)   
    acc_number = db.Column(db.String(8), nullable=False)  

    def __init__(self, acc_name, bank_name, sort_code, acc_number):
        BaseEntity.__init__(self) 
        
        self. acc_name = acc_name
        self.bank_name = bank_name
        self.sort_code = sort_code
        self.acc_number = acc_number