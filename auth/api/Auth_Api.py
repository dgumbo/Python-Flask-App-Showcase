from flask import Blueprint, render_template, request, redirect
from auth.service.User_Service import UserService
from auth.models.User import User
from common.exceptions.Custom_Exceptions import BadLoginCredentialsException

from flask_login import login_required  
   
auth_api = Blueprint('auth_api', __name__) 
api_root='/auth'
template_folder='/auth'

userService = UserService()
 
    
@auth_api.route('/login', methods=['GET', 'POST'])
def handle_login():
    data = request.form   
    args = request.args
 
    redirect_url = None
 
    if 'next' in args and request.method == 'GET':
        redirect_url = request.args['next']
    elif 'redirect_url' in data :
        redirect_url = data['redirect_url'] 


    if request.method == 'GET':  
        return render_template(f"{template_folder}/login.html", api_root=api_root, redirect_url = redirect_url)
    else : 
        email = data['email']
        username = email
        password = data['password'] 
        user = User(username, email, password)

        try :
            if userService.authenticate(username, email, password) : 
                if redirect_url == None:
                    redirect_url = '/home' 

                return redirect( redirect_url )
        
        except BadLoginCredentialsException as err:
            return render_template(f"{template_folder}/login.html", api_root=api_root, err_msg="Bad Login Credentials")


@auth_api.route('/signup', methods=['GET'])
def signup():
    return render_template(f"{template_folder}/signup.html", api_root=api_root)
    

@auth_api.route('/signup', methods=['POST'])
def handle_signup():
    data = request.form
    
    email = data['email']
    username = email
    password = data['password']
    user = User(username, email, password)

    userService.create(user)

    return redirect( f'{api_root}/login' )
    
@login_required
@auth_api.route('/delete', methods=['POST'])
def handle_delete(): 
    data = request.form
    
    delete_id = data['delete_id']  
    userService.delete(delete_id)

    return redirect( f'{api_root}/user-list' )


@auth_api.route('/user-list', methods=['GET'])
@login_required
def view_user_list():    
    users = userService.get_all()  
    return render_template(f"{template_folder}/user-list.html", users=users, api_root=api_root)


@auth_api.route('/logout', methods=['GET'])
@login_required
def logout_handler():    
    userService.logout_user()
    return redirect( '/' )
    
 
