from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseEntity( db.Model ):

    id = db.Column(db.Integer, primary_key=True)   
    active_status = db.Column(db.Integer)  
    created_by = db.Column(db.String)  
    creation_time = db.Column(db.String)  
    updated_by = db.Column(db.String)  
    update_time = db.Column(db.String)  

    def __init__(self, id=0, active_status=True, created_by="", creation_time="", updated_by="", update_time=""):
        self.id=id 
        self.active_status=active_status 
        self.created_by=created_by
        self.creation_time=creation_time
        self.updated_by=updated_by
        self.update_time=update_time
        

    def __repr__(self) :
        classname = type(self)
        return f"{classname} is {self.id}"


