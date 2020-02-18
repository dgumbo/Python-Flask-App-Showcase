from flask import Blueprint, render_template, request, redirect
from invoice.services.Invoice_Service import InvoiceService 
   
invoice_api = Blueprint('invoice_api', __name__) 

invoiceService = InvoiceService()

template_files_path = "/invoices" 
api_root = "/invoices"

@invoice_api.route('/', methods=['GET'])
def list():
    invoices = invoiceService.get_all()
    return render_template(f"{template_files_path}/invoice-list.html", invoices=invoices, api_root=api_root)


@invoice_api.route('/create', methods=['GET'])
def create():
    return render_template(f"{template_files_path}/create-invoice.html", api_root=api_root)    


@invoice_api.route('/create', methods=['POST'])
def handle_create():
    entity = request.form
    invoiceService.create(entity) 
    print("entity was sucesifuly created")
    return redirect( f'{api_root}'  )

    
 
