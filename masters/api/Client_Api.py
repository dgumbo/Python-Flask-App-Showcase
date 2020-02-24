from flask import Blueprint, render_template, request, redirect
from masters.services import ClientService 
from masters.models.Client import Client
from auth.models.User import User
from flask_login.utils import _get_user
   
client_api = Blueprint('client_api', __name__) 
logged_in_user : User

@client_api.before_request
def restrict_to_logged_in_users(): 
    logged_in_user = _get_user() 
    if logged_in_user == None or logged_in_user.is_authenticated == False:
        return redirect('/auth/login')


template_files_path = "/clients" 
api_root = "/clients"
clientService = ClientService()

@client_api.route('/', methods=['GET'])
def list():
    clients = clientService.get_all()
    return render_template(f"{template_files_path}/client-list.html", clients=clients, api_root=api_root) 


@client_api.route('/create', methods=['GET'])
def create():
    return render_template(f"{template_files_path}/create-client.html", api_root=api_root)    


@client_api.route('/create', methods=['POST'])
def handle_create():
    data = request.form 
        
    name = data['name']
    phone = data['phone']
    address_1 = data['address_1'] 
    address_2 = data['address_2']
    city = data['city']
    post_code = data['post_code'] 

    client = Client(_get_user(), name, phone, address_1, address_2, city, post_code)
    clientService.create(client) 
    print("entity was sucesifuly created")
    return redirect( f'{api_root}'  )

     
@client_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    clientService.delete(delete_id)

    return redirect( f'{api_root}' )

    
 
