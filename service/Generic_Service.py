from common.models.Base_Entity import BaseEntity 
from common.exceptions.Custom_Exceptions import EntityNotSubClassOfBaseEntity_Error

class GenericService:

    def __init__(self):
        pass  
    
    # def return_common_api(genericService : GenericService, api_route, child_api_name) -> BaseEntity : 

    def create(self, entity:BaseEntity):       
        if isinstance(entity, BaseEntity) :
            return BaseEntity() #"Test User1", "Passwor1")
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def update(self, entity:BaseEntity, id):        
        if isinstance(entity, BaseEntity) :
            return BaseEntity() #"Test User1", "Passwor1")
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def delete(self, entity:BaseEntity):        
        if isinstance(entity, BaseEntity) :
            print (f"printing user on create user:  ") 
        # else :
        #     raise EntityNotSubClassOfBaseEntity_Error("An error occurred. Entity does not extend BaseEntity")
 
    def find(self, id):        
        return BaseEntity() #"Test User1", "Passwor1")
       
    def get_all(self) :
        entities = []
        entity1 = BaseEntity() #"Test User1", "Passwor1")
        entity2 = BaseEntity() #"Test User2", "Passwor1")

        entities.append(entity1)
        entities.append(entity2)

        return entities
         