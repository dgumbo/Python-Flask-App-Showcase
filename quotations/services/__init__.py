from common.service.Generic_Service import GenericService
from common.db.Base_CRUD import BaseCrud

from masters.models.Company import Company 
from masters.models.Client import Client 
from masters.models.Payment_Detail import PaymentDetail
from masters.models.Product import Product
from masters.models.Service import Service 

class CompanyService(GenericService):

    def __init__(self): 
        crud = BaseCrud( Company ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Company ) 
 

class PaymentDetailsService(GenericService):

    def __init__(self):
        crud = BaseCrud( PaymentDetail ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  PaymentDetail )  


class ProductsService(GenericService): 

    def __init__(self):
        crud = BaseCrud( Product ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Product )   

        
class ServicesService(GenericService):

    def __init__(self):
        crud = BaseCrud( Service ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Service )      

   
class ClientService(GenericService):

    def __init__(self):
        crud = BaseCrud( Client ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Client )     