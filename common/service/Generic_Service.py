from common.models.Base_Entity import BaseEntity 
from common.exceptions.Custom_Exceptions import EntityNotSubClassOfBaseEntity_Error
from common.db.Base_CRUD import BaseCrud

class GenericService: 

    def __init__(self, entityCrud : BaseCrud):
        self.entityCrud = entityCrud  
    
    # def return_common_api(genericService : GenericService, api_route, child_api_name) -> BaseEntity : 

    def create(self, entity:BaseEntity):       
        return self.entityCrud.create(entity)  
        # if isinstance(entity, BaseEntity) :
        #     return self.entityCrud.find_all()  #"Test User1", "Passwor1")
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def update( self, entity:BaseEntity, id:int ):        
        return self.entityCrud.update( entity, id )
        # if isinstance(entity, BaseEntity) :
        #     return BaseEntity() #"Test User1", "Passwor1")
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def delete(self, entity:BaseEntity):      
        return self.entityCrud.delete(entity)  
        # if isinstance(entity, BaseEntity) :
        #     print (f"printing user on create user:  ") 
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def find(self, id):        
        return self.entityCrud.find(id)  
       
    def get_all(self) :
        return self.entityCrud.find_all() 
       
    def get_all_json(self) :  
        entity_list = self.entityCrud.find_all()  
  
        entity_list_json = []
        for entity in entity_list:   
            entity_list_json.append(entity.json())  

        return entity_list_json