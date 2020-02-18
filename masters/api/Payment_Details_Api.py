from flask import Blueprint, render_template, request, redirect
from masters.services.Payment_Details_Service import PaymentDetailsService 
   
payment_details_api = Blueprint('payment_details_api', __name__) 

paymentDetailService = PaymentDetailsService()

template_files_path = "/payment-details" 
payment_details_api_root = "/payment-details"

@payment_details_api.route('/', methods=['GET'])
def payment_detail_list():
    payment_details = paymentDetailService.get_all()
    return render_template(f"{template_files_path}/payment-details-list.html", payment_details=payment_details, payment_details_api_root=payment_details_api_root)


@payment_details_api.route('/create-payment-detail', methods=['GET'])
def create_payment_detail():
    return render_template(f"{template_files_path}/create-payment-detail.html", payment_details_api_root=payment_details_api_root)    


@payment_details_api.route('/create-payment-detail', methods=['POST'])
def handle_create_payment_detail():
    payment_detail = request.form
    paymentDetailService.create(payment_detail) 
    print("payment_detail was sucesifuly created")
    return redirect( f'{payment_details_api_root}'  )

    
 
