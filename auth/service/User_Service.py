from auth.models.User import User

class UserService:

    def create_user(self, user):        
        print (f"printing user on create user: {user['email']}") 

    def authenticate(self, user):
        pass

    def get_all_users(self):
        users = []
        user1 = User("Test User1", "Passwor1")
        user2 = User("Test User2", "Passwor1")

        users.append(user1)
        users.append(user2)

        return users