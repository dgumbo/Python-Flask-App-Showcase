from flask_sqlalchemy import SQLAlchemy 
from flask_sqlalchemy import Model
from flask_migrate import Migrate
  
class BDMigrate :

    def __init__(self, db: SQLAlchemy , model : Model ) :
        self.db = db
        self.model = model

    ## Find All ###
    def find_all(self):  
        entities = self.model.query.all()
        return entities

    ## Find ###
    def find(self, id:int):   
        entity = self.model.query.get(id)
        return entity

    ## Create ###
    def create(self, entity):  
        self.db.session.add(entity)
        self.db.session.commit()

        return entity

    ## Update ###
    def update(self, entity,  id:int):   
        upd_entity = self.model.get(id)
        
        self.db.session.delete(entity)
        self.db.session.commit()

        return upd_entity

    ## Delete ###
    def delete(self, entity):   
        del_entity = self.model.get(entity.id)

        self.db.session.add(del_entity)
        self.db.session.commit()

        return True