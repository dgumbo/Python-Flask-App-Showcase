from flask import Blueprint, render_template, request, redirect
from masters.services.Company_Service import CompanyService 
from common.service.Generic_Service import GenericService

def return_common_api(genericService : GenericService, api_route, child_api_name) -> Blueprint : 
 
    return_api = Blueprint(api_route, child_api_name)  

    return return_api

    # template_files_path = "/client-company" 
    # return_api_root = "/company-setup"

    # @return_api.route('/', methods=['GET'])
    # def company_list():
    #     companies = companyService.get_all()
    #     return render_template(f"{template_files_path}/company-list.html", companies=companies, return_api_root=return_api_root)


    # @return_api.route('/create-company', methods=['GET'])
    # def create_company():
    #     return render_template(f"{template_files_path}/create-company.html", return_api_root=return_api_root)    

    # @return_api.route('/create-company', methods=['POST'])
    # def handle_create_company():
    #     company = request.form
    #     companyService.create(company) 
    #     print("company was sucesifuly created")
    #     return redirect( f'{return_api_root}'  )

    
 
