from common.models.Base_Entity import BaseEntity, db

class User(BaseEntity, db.Model): 
    email = db.Column(db.String(50), unique=True, nullable=False)  
    password = db.Column(db.String(50), nullable=False)  
    
    def __init__(self, email, password):
        BaseEntity.__init__(self)
        self.email = email
        self.password = password 