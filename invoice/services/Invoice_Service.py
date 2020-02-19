from common.service.Generic_Service import GenericService
from common.db.Base_CRUD import BaseCrud

from invoice.models.Invoice import Invoice 

class InvoiceService(GenericService): 

    def __init__(self): 
        crud = BaseCrud( Invoice ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  Invoice ) 