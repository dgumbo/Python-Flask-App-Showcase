from masters.models.Company import Company 
from common.service.Generic_Service import GenericService
from common.db.Base_CRUD import BaseCrud

class CompanyService(GenericService):

    def __init__(self): 
        crud = BaseCrud( Company ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Company ) 
 
