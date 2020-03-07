from flask import Blueprint, render_template, request, redirect
from masters.services import ProductsService , ServicesService
from masters.models.Product import Product
from masters.models.Service import Service
   
from flask_login.utils import _get_user

products_api = Blueprint('products_api', __name__) 

@products_api.before_request
def restrict_to_logged_in_users(): 
    logged_in_user = _get_user() 
    if logged_in_user == None or logged_in_user.is_authenticated == False:
        return redirect('/auth/login')

products_api_root = "/products"
productsService = ProductsService()

@products_api.route('/', methods=['GET'])
def product_list():
    products = productsService.get_all()
    return render_template("/products/product-list.html", products=products, api_root=products_api_root)


@products_api.route('/create', methods=['GET'])
def create_product():
    return render_template("/products/create-product.html", api_root=products_api_root)    


@products_api.route('/create', methods=['POST'])
def handle_create_product():
    data = request.form 
        
    name = data['name']
    description = data['description']
    price = data['price'] 

    product = Product(_get_user(), name, description, price)

    productsService.create(product) 
    return redirect( f'{products_api_root}'  )

     
@products_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    productsService.delete(delete_id)

    return redirect( f'{products_api_root}' )
    
 


services_api = Blueprint('services_api', __name__)    

@services_api.before_request
def restrict_services_api_to_logged_in_users(): 
    logged_in_user = _get_user() 
    if logged_in_user == None or logged_in_user.is_authenticated == False:
        return redirect('/auth/login')

service_api_root = "/services"
servicesService = ServicesService()

@services_api.route('/', methods=['GET']) 
def service_list():
    services = servicesService.get_all()
    return render_template("/products/service-list.html", services=services, api_root=service_api_root)
     
 
@services_api.route('/create', methods=['GET'])
def create_service():
    return render_template("/products/create-service.html", api_root=service_api_root)    


@services_api.route('/create', methods=['POST'])
def handle_create_service():
    data = request.form 
        
    name = data['name']
    description = data['description']
    charge = data['charge'] 

    service = Service(_get_user(), name, description, charge)
    servicesService.create(service) 
    return redirect( f'{service_api_root}'  )

     
@services_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    servicesService.delete(delete_id)

    return redirect( f'{service_api_root}' )