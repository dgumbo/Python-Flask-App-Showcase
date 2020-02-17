from common.model.Base_Entity import BaseEntity

class User(BaseEntity):
    
    def __init__(self, email, password):
        BaseEntity.__init__(self)
        self.email = email
        self.password = password 