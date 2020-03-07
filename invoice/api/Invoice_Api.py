from flask import Blueprint, render_template, request, redirect
from invoice.services.Invoice_Service import InvoiceService 
from flask_login.utils import _get_user
from invoice.models.Invoice import Invoice
from flask import jsonify
   
invoice_api = Blueprint('invoice_api', __name__) 

invoiceService = InvoiceService()

template_files_path = "/invoices" 
api_root = "/invoices"

@invoice_api.route('/', methods=['GET'])
def list():
    invoices = invoiceService.get_all()
    return render_template(f"{template_files_path}/invoice-list.html", invoices=invoices, api_root=api_root)

from auth.models.User import User
@invoice_api.route('/create', methods=['GET'])
def create():
    user:User = _get_user()
    invoice = Invoice()
    # print("\n\n\n")
    # print(user)
    # print("\n")
    # print(user.companies)
    # print("\n")
    # print(user.invoices)
    # print("\n")
    # print(user.paymentDetails)
    # print("\n")
    # print(user.services)
    # print("\n")
    # print(user.products)
    # print("\n\n\n")

    return render_template(f"{template_files_path}/create-invoice.html", api_root=api_root, user=user, invoice=invoice)    


@invoice_api.route('/create', methods=['POST'])
def handle_create():
    data = request.form 
        
    name = data['name']
    description = data['description']
    charge = data['charge'] 

    invoice = Service(_get_user(), name, description, charge) 
    invoiceService.create(invoice) 
    print("entity was sucesifuly created")
    return redirect( f'{api_root}'  )

    
 
 
# Select Trading Name to Show on Invoice
# Select Payment details

# Invoice Effective Date

# Select services 
# service subtotal
# selet products 
# product sub total

# grand total