from flask import Blueprint, render_template, request, redirect
from masters.services import PaymentDetailsService 
from masters.models.Payment_Detail import PaymentDetail 

from flask_login.utils import _get_user

payment_details_controller = Blueprint('payment_details_controller', __name__) 

@payment_details_controller.before_request
def restrict_to_logged_in_users(): 
    logged_in_user = _get_user() 
    if logged_in_user == None or logged_in_user.is_authenticated == False:
        return redirect('/auth/login')

paymentDetailService = PaymentDetailsService()

template_files_path = "/payment-details" 
api_root = "/payment-details"

@payment_details_controller.route('/', methods=['GET'])
def payment_detail_list():
    payment_details = paymentDetailService.get_all()
    return render_template(f"{template_files_path}/payment-details-list.html", payment_details=payment_details, api_root=api_root)


@payment_details_controller.route('/create', methods=['GET'])
def create_payment_detail():
    return render_template(f"{template_files_path}/create-payment-detail.html", api_root=api_root)    


@payment_details_controller.route('/create', methods=['POST'])
def handle_create_payment_detail():
    data = request.form
    
    acc_name = data['acc_name']
    bank_name = data['bank_name']
    sort_code = data['sort_code']
    acc_number = data['acc_number']

    payment_detail = PaymentDetail(_get_user(), acc_name, bank_name, sort_code, acc_number)
    paymentDetailService.create(payment_detail) 
    print("payment_detail was sucesifuly created")
    return redirect( f'{api_root}'  )

      
@payment_details_controller.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    paymentDetailService.delete(delete_id)

    return redirect( f'{api_root}' )
 



from flask_restful import Resource, Api

from flask.json import JSONEncoder

from typing import List

import json

from json import JSONEncoder

jsonEncoder = JSONEncoder()

class PaymentDetailApi(Resource): 

    def get(self):
        payment_details_json = paymentDetailService.get_all_json()
    
        return payment_details_json
    
    # def get(self, get_id):
    #     # data = request.form
        
    #     # get_id = data['get_id']  
    #     payment_detail = paymentDetailService.delete(get_id)

    #     return payment_detail

    # def post(self):
    #     data = request.form
        
    #     acc_name = data['acc_name']
    #     bank_name = data['bank_name']
    #     sort_code = data['sort_code']
    #     acc_number = data['acc_number']

    #     payment_detail = PaymentDetail(_get_user(), acc_name, bank_name, sort_code, acc_number)
    #     payment_detail = paymentDetailService.create(payment_detail) 
    #     print("payment_detail was sucesifuly created")
    #     return payment_detail
 
    # def delete(self): 
    #     data = request.form
        
    #     delete_id = data['delete_id']  
    #     payment_detail = paymentDetailService.delete(delete_id)

    #     return payment_detail