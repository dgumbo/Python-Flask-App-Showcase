from masters.models.Payment_Detail import PaymentDetail
from common.service.Generic_Service import GenericService
from common.db.Base_CRUD import BaseCrud

class PaymentDetailsService(GenericService):

    def __init__(self):
        crud = BaseCrud( PaymentDetail ) 
        GenericService.__init__(self, crud ) #entityCrud : BaseCrud
        self.crud = BaseCrud(  PaymentDetail )   
         




# acc_name
# bank_name
# sort_code
# acc_number