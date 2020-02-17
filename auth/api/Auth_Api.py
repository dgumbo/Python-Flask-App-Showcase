from flask import Blueprint, render_template, request, redirect
from auth.service.User_Service import UserService
from auth.models.User import User
   
auth_api = Blueprint('auth_api', __name__) 

userService = UserService()

@auth_api.route('/login', methods=['GET'])
def login():
    return render_template("/auth/login.html")
    

@auth_api.route('/login', methods=['POST'])
def handle_login():
    user = request.form 
    userService.authenticate(user)

    return redirect( '/home' )


@auth_api.route('/signup', methods=['GET'])
def signup():
    return render_template("/auth/signup.html")
    

@auth_api.route('/signup', methods=['POST'])
def handle_signup():
    user = request.form
    userService.create_user(user)

    return redirect( '/auth/login' )

@auth_api.route('/user-list', methods=['GET'])
def view_user_list():
    
    users = userService.get_all_users()  

    return render_template("/auth/user-list.html", users=users)
    
 
