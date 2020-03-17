from flask import Blueprint, render_template, request, redirect

   
from flask_login.utils import _get_user

quotation_api = Blueprint('quotation_api', __name__)  

# @products_api.before_request
# def restrict_to_logged_in_users(): 
#     logged_in_user = _get_user() 
#     if logged_in_user == None or logged_in_user.is_authenticated == False:
#         return redirect('/auth/login')

# products_api_root = "/products"
# productsService = ProductsService()

# @products_api.route('/', methods=['GET'])
# def product_list():
#     products = productsService.get_all()
#     return render_template("/products/product-list.html", products=products, api_root=products_api_root)


# @products_api.route('/update/<update_id>', methods=['GET'])
# def update_product(update_id): 

#     product = productsService.find(update_id)
#     return render_template("/products/create-product.html", update_id=update_id, product=product, api_root=products_api_root) 


# @products_api.route('/update/<update_id>', methods=['POST'])
# def update_product_post(update_id): 
#     data = request.form 

#     name = data['name']
#     description = data['description']
#     price = data['price'] 

#     product = productsService.find(update_id)
#     product.name=name
#     product.description=description
#     product.price=price

#     productsService.update(product, update_id) 
#     return redirect( f'{products_api_root}'  )

# @products_api.route('/create', methods=['GET'])
# def create_product():
#     # product = Product()
#     return render_template("/products/create-product.html", update_id=0, product=None, api_root=products_api_root)    


# @products_api.route('/create', methods=['POST'])
# def handle_create_product():
#     data = request.form 
        
#     name = data['name']
#     description = data['description']
#     price = data['price'] 

#     product = Product(_get_user(), name, description, price)

#     productsService.create(product) 
#     return redirect( f'{products_api_root}'  )

     
# @products_api.route('/delete', methods=['POST'])
# def handle_delete(): 
#     data = request.form
    
#     delete_id = data['delete_id']  
#     productsService.delete(delete_id)

#     return redirect( f'{products_api_root}' )