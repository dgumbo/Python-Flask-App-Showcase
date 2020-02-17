from flask import Blueprint, render_template, request, redirect
from products.services.Products_Service import ProductsService 
   
products_api = Blueprint('products_api', __name__) 

productsService = ProductsService()

@products_api.route('/product-list', methods=['GET'])
def product_list():
    products = productsService.get_all_products()
    return render_template("/products/product-list.html", products=products)


@products_api.route('/create-product', methods=['GET'])
def create_product():
    return render_template("/products/create-product.html")    


@products_api.route('/create-product', methods=['POST'])
def handle_create_product():
    product = request.form
    productsService.create_product(product) 
    return redirect( '/products-services/product-list'  )


@products_api.route('/service-list', methods=['GET']) 
def service_list():
    services = productsService.get_all_services()
    return render_template("/products/service-list.html", services=services)


@products_api.route('/create-service', methods=['GET'])
def create_service():
    service = request.form
    productsService.create_service(service) 
    return render_template("/products/create-service.html")    
    

@products_api.route('/create-service', methods=['POST'])
def handle_create_service(): 
    return redirect( '/products-services/service-list' )
    
 
