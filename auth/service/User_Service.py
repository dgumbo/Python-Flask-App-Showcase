from auth.models.User import User, db
from common.db.Base_CRUD import BaseCrud
from common.service.Generic_Service import GenericService
from common.exceptions.Custom_Exceptions import BadLoginCredentialsException 

from db_holder import loginManager
from flask_login import login_required, login_user, logout_user
from flask_login.utils import _get_user


class UserService (GenericService):
   
    def __init__(self):
        crud = BaseCrud( User ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  User )   

    @loginManager.user_loader
    def load_user(user_id): 
        return User.query.get(user_id) 
         
    def authenticate(self, username, email, password) -> bool:
        if username == None or password == None:
            raise  BadLoginCredentialsException()  

        db_user_to_login = self.find_user_by_email( email )
 
        if db_user_to_login == None :
            raise  BadLoginCredentialsException()  
        elif db_user_to_login.check_password( password ) == False :
            raise  BadLoginCredentialsException() 
             
        login_user(db_user_to_login) 

        return True
 
 
    def find_user_by_email(self, email ) -> User:
        users = User.query.filter_by(email=email) 
        users = users.all()
 
        if len(users) >= 1 :
            return users[0]
        else:
            return None 

 
    def find_user_by_username(self, email ) -> User:
        users = User.query.filter_by(username=username) 
        users = users.all()
 
        if len(users) >= 1 :
            return users[0]
        else:
            return None 

    def logout_user(self):
        logout_user()

    def get_logged_in_user(self):
        logged_in_user = _get_user()
        return logged_in_user
