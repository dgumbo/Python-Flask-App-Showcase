from db_holder import db
from datetime import datetime
 

class BaseEntity( object ): 

    id = db.Column(db.Integer, primary_key=True)   
    active_status = db.Column(db.Boolean, nullable=False)  
    created_by = db.Column(db.String, nullable=False)  
    creation_time = db.Column(db.DateTime, nullable=False)  
    updated_by = db.Column(db.String, nullable=False)  
    update_time = db.Column(db.DateTime, nullable=False)  


    def __init__(self ):
        self.active_status = True  


    def __repr__(self) :
        classname = self.__class__.__name__
        return f"{classname}; ID: {self.id}, Active Status: {self.active_status}, Created by: {self.created_by}, on: {self.creation_time}"


    def pre_update(self): 
        now = datetime.now()
        if self.created_by == None :
            self.created_by = ""
        if self.creation_time == None :
            self.creation_time = now  
        if self.updated_by == None :
            self.updated_by = ""
        if self.update_time == None :
            self.update_time = now 
 

    def json(self):
        return {
            'id': self.id, 
            'active_status': self.active_status,
            'created_by': self.created_by,
            # 'creation_time':   self.creation_time,
            'updated_by': self.updated_by,
            # 'update_time': self.update_time,
        }   
 
        # "items": [item.json() for item in self.items.all()],
