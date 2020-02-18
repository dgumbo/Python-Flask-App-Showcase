from common.models.Base_Entity import BaseEntity, db 

class Puppy( BaseEntity, db.Model ) :
 
    name = db.Column(db.String)    

    def __init__(self, name): 
        BaseEntity.__init__(self)
        self.name=name  
         
    def __repr__(self) :
        classname = type(self)
        return f"Id : {self.id}, Name : {self.name}"


