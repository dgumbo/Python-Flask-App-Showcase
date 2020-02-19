from flask import Blueprint, render_template, request, redirect
from masters.services import ProductsService , ServicesService
   
from flask_login.utils import _get_user

products_and_services_api = Blueprint('products_and_services_api', __name__) 

@products_and_services_api.before_request
def restrict_to_logged_in_users(): 
    logged_in_user = _get_user() 
    if logged_in_user == None or logged_in_user.is_authenticated == False:
        return redirect('/auth/login')

productsService = ProductsService()
servicesService = ServicesService()

@products_and_services_api.route('/product-list', methods=['GET'])
def product_list():
    products = productsService.get_all()
    return render_template("/products/product-list.html", products=products)


@products_and_services_api.route('/create-product', methods=['GET'])
def create_product():
    return render_template("/products/create-product.html")    


@products_and_services_api.route('/create-product', methods=['POST'])
def handle_create_product():
    product = request.form
    productsService.create(product) 
    return redirect( '/products-services/product-list'  )


@products_and_services_api.route('/service-list', methods=['GET']) 
def service_list():
    services = servicesService.get_all()
    return render_template("/products/service-list.html", services=services)


@products_and_services_api.route('/create-service', methods=['GET'])
def create_service():
    service = request.form
    servicesService.create(service) 
    return render_template("/products/create-service.html")    
    

@products_and_services_api.route('/create-service', methods=['POST'])
def handle_create_service(): 
    return redirect( '/products-services/service-list' )
    
 
