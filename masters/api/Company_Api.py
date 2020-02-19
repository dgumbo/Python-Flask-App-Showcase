from flask import Blueprint, render_template, request, redirect
from masters.services import CompanyService 
from masters.models.Company import Company
   
company_api = Blueprint('company_api', __name__) 

companyService = CompanyService()

template_files_path = "/company-setup" 
api_root = "/company-setup"


@company_api.route('/', methods=['GET'])
def company_list():
    companies = companyService.get_all()
    return render_template(f"{template_files_path}/company-list.html", companies=companies, api_root=api_root)


@company_api.route('/create', methods=['GET'])
def create_company():
    return render_template(f"{template_files_path}/create-company.html", api_root=api_root)    

@company_api.route('/create', methods=['POST'])
def handle_create_company():
    data = request.form 
        
    trading_name = data['trading_name']
    contact_person = data['contact_person']
    email = data['email']
    phone = data['phone']
    address_ln_1 = data['address_ln_1']
    address_ln_2 = data['address_ln_2']
    city = data['city']
    postal_code = data['postal_code']

    company = Company(trading_name, contact_person, email, phone, address_ln_1, address_ln_2, city, postal_code)

    companyService.create(company) 
    print("company was sucesifuly created")
    return redirect( f'{api_root}'  )

     
@company_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    companyService.delete(delete_id)

    return redirect( f'{api_root}' )
 
