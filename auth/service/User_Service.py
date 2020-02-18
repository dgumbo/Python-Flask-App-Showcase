from auth.models.User import User, db
from common.db.Base_CRUD import BaseCrud
from common.service.Generic_Service import GenericService

class UserService (GenericService):
  
    def __init__(self):
        crud = BaseCrud( User ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        # self.crud = BaseCrud( db, User )   

    def authenticate(self, user):
        pass

    # def create_user(self, user):        
    #     print (f"printing user on create user: {user['email']}") 
 
    # def get_all_users(self):
    #     users = self.crud.find_all() 

    #     return users