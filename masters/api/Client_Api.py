from flask import Blueprint, render_template, request, redirect
from masters.services import ClientService 
   
client_api = Blueprint('client_api', __name__) 

clientService = ClientService()

template_files_path = "/clients" 
api_root = "/clients"

@client_api.route('/', methods=['GET'])
def list():
    clients = clientService.get_all()
    return render_template(f"{template_files_path}/client-list.html", clients=clients, api_root=api_root) 


@client_api.route('/create', methods=['GET'])
def create():
    return render_template(f"{template_files_path}/create-client.html", api_root=api_root)    


@client_api.route('/create', methods=['POST'])
def handle_create():
    entity = request.form
    clientService.create(entity) 
    print("entity was sucesifuly created")
    return redirect( f'{api_root}'  )

    
 
