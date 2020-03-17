from flask import Blueprint, render_template, request, redirect
from invoice.services.Invoice_Service import InvoiceService 
from flask_login.utils import _get_user
from invoice.models.Invoice import Invoice

from flask import jsonify

from flask_restful import Api, Resource
   
invoice_controller = Blueprint('invoice_controller', __name__) 

invoiceService = InvoiceService()

template_files_path = "/invoices" 
controller_root = "/invoices"
api_root = controller_root + '/api'

@invoice_controller.route('/', methods=['GET'])
def list():
    invoices = invoiceService.get_all()
    return render_template(f"{template_files_path}/invoice-list.html", invoices=invoices, controller_root=controller_root)

from auth.models.User import User
@invoice_controller.route('/create', methods=['GET'])
def create():
    user:User = _get_user()
    invoice = Invoice() 

    return render_template(f"{template_files_path}/create-invoice.html", controller_root=controller_root, api_root=api_root, user=user, invoice=invoice)    


@invoice_controller.route('/create', methods=['POST'])
def handle_create():
    data = request.form 
        
    name = data['name']
    description = data['description']
    charge = data['charge'] 

    invoice = invoiceService.create (_get_user(), name, description, charge) 
    invoiceService.create(invoice) 
    print("entity was sucesifuly created")
    return redirect( f'{controller_root}'  )

    
 
class InvoiceApi(Resource) :
    def get(self, id):
        invoice = invoiceService.find(id)

        return invoice

    def put(self, id):
        pass

    def delete(self, id):
        pass
 
class InvoiceListApi(Resource) :
    def get(self):
        invoices = invoiceService.get_all()

        return invoices



invoice_api = Api( invoice_controller )
invoice_api.add_resource(InvoiceListApi, '/api', endpoint = 'invoices')
invoice_api.add_resource(InvoiceApi, '/api/<int:id>', endpoint = 'invoice')