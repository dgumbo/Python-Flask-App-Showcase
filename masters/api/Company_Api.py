from flask import Blueprint, render_template, request, redirect
from masters.services.Company_Service import CompanyService 
   
company_api = Blueprint('company_api', __name__) 

companyService = CompanyService()

template_files_path = "/company-setup" 
company_api_root = "/company-setup"


@company_api.route('/', methods=['GET'])
def company_list():
    companies = companyService.get_all()
    return render_template(f"{template_files_path}/company-list.html", companies=companies, company_api_root=company_api_root)


@company_api.route('/create-company', methods=['GET'])
def create_company():
    return render_template(f"{template_files_path}/create-company.html", company_api_root=company_api_root)    

@company_api.route('/create-company', methods=['POST'])
def handle_create_company():
    company = request.form
    companyService.create(company) 
    print("company was sucesifuly created")
    return redirect( f'{company_api_root}'  )

    
 
