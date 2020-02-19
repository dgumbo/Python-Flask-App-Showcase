from flask_sqlalchemy import SQLAlchemy 
from flask_sqlalchemy import Model
from db_holder import db
from common.models.Base_Entity import BaseEntity
  
class BaseCrud :

    def __init__(self, model : Model ) : 
        self.model = model
        self.db = db

    ## Find All ###
    def find_all(self):  
        entities = self.model.query.all()
        return entities

    ## Find ###
    def find(self, id:int):   
        entity = self.model.query.get(id)
        return entity

    ## Create ###
    def create(self, entity:BaseEntity):  
        entity.pre_update()
        self.db.session.add(entity)
        self.db.session.commit()

        return entity

    ## Update ###
    def update(self, entity:BaseEntity, update_id:int):   
        upd_entity = self.model.query.get( update_id )
        
        entity.pre_update()
        db.session.update(entity)
        self.db.session.commit()

        return upd_entity

    ## Delete ###
    def delete(self, delete_id:int):    
        del_entity = self.model.query.get(delete_id)

        self.db.session.delete(del_entity)
        self.db.session.commit()

        return True