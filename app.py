# pip freeze > requirements.txt
 
import os
import click
from flask.cli import with_appcontext
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome  
from flask_datepicker import datepicker
from flask_login import LoginManager
from flask_login import login_required, login_user, logout_user
 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_cors import CORS

from db_holder import InitializeDBConnection, db, loginManager
 
 
__version__ = (1, 0, 0, "dev") 

# def create_app(test_config=None):
"""Create and configure an instance of the Flask application."""
app = Flask(__name__) #, instance_relative_config=True)

Bootstrap( app ) 
FontAwesome( app )
datepicker( app )

InitializeDBConnection( app )
db.init_app( app )

Migrate( app, db )

app.config['SECRET_KEY'] = 'mysecretkey' 
loginManager.login_view = '/auth/login'
loginManager.init_app(app)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route( '/home' )
def home():
    return redirect("/")
    
@app.route( '/' )
def index():
    return render_template("home.html")
        

from auth.api.Auth_Api import auth_api
app.register_blueprint(auth_api, url_prefix='/auth')
    
from masters.api.Payment_Details_Api import payment_details_api
app.register_blueprint(payment_details_api, url_prefix='/payment-details')

from masters.api.Company_Api import company_api
app.register_blueprint(company_api, url_prefix='/company-setup')

from masters.api.Products_Services_Api import products_api
app.register_blueprint(products_api, url_prefix='/products')

from masters.api.Products_Services_Api import services_api
app.register_blueprint(services_api, url_prefix='/services')

from invoice.api.Invoice_Api import invoice_controller
app.register_blueprint(invoice_controller, url_prefix='/invoices')

from masters.api.Client_Api import client_api
app.register_blueprint(client_api, url_prefix='/clients')

# app.cli.add_command(init_db_command)

@app.errorhandler(404)
def errorhandler(e):
    return render_template("error-handler/not-found-handler.html", error=e)
  

@app.route('/init-db')
def init_db_handler():    
    init_db()
    return redirect("/auth/init-test-user") 

@app.route('/reset-db')
def reset_db_handler():     
    drop_and_init_db()
    return redirect("/") 

def init_db():     
    print ('\n\n\nStarting Database Initialization')
    print (db.get_binds()) 
    db.create_all()  
    print ('Database Was initialized succesifully\n\n\n')

def drop_and_init_db():     
    print ('\n\n\nStarting Database  Drop All')
    print (db.get_binds())
    db.drop_all() 
    print ('Finished Database Drop All')
    print ('Starting Database Initialization')
    db.create_all()  
    print ('Database Was initialized succesifully\n\n\n')
 

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db() 
 

if __name__ == "__main__" : 
    print("\n*  Starting App!\n") 
    # app = create_app()
    
    app.run(debug=True) 