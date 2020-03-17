from common.models.Base_Entity import BaseEntity, db
from auth.models.User import User
from flask_restful import Resource

class Quotation(BaseEntity, db.Model, Resource):
      
    def __init__(self ):
        BaseEntity.__init__(self)  

        # name description cost