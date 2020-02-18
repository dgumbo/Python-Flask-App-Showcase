from flask import Blueprint, render_template, request, redirect
from auth.service.User_Service import UserService
from auth.models.User import User
   
auth_api = Blueprint('auth_api', __name__) 
api_root='/auth'
template_folder='/auth'

userService = UserService()

@auth_api.route('/login', methods=['GET'])
def login():
    return render_template(f"{template_folder}/login.html", api_root=api_root)
    

@auth_api.route('/login', methods=['POST'])
def handle_login():
    user = request.form 
    userService.authenticate(user)

    return redirect( '/home' )


@auth_api.route('/signup', methods=['GET'])
def signup():
    return render_template(f"{template_folder}/signup.html", api_root=api_root)
    

@auth_api.route('/signup', methods=['POST'])
def handle_signup():
    data = request.form
    
    email = data['email']
    password = data['password']
    user = User(email, password)

    userService.create(user)

    return redirect( f'{api_root}/login' )
    

@auth_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    userService.delete(delete_id)

    return redirect( f'{api_root}/user-list' )


@auth_api.route('/user-list', methods=['GET'])
def view_user_list():    
    users = userService.get_all()  
    return render_template(f"{template_folder}/user-list.html", users=users, api_root=api_root)
    
 
