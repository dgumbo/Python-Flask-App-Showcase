from common.models.Base_Entity import BaseEntity, db

class User(BaseEntity): 
    email = db.Column(db.String)  
    password = db.Column(db.String)  
    
    def __init__(self, email, password):
        BaseEntity.__init__(self)
        self.email = email
        self.password = password 