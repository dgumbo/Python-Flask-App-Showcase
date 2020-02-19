# pip freeze > requirements.txt # Remove pyodbc
 
import click
from flask.cli import with_appcontext
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome  
from flask_login import LoginManager
from flask_login import login_required, login_user, logout_user
 
from flask_sqlalchemy import SQLAlchemy

from db_holder import db, loginManager
 
__version__ = (1, 0, 0, "dev") 

import os
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    Bootstrap(app) 
    FontAwesome(app)
 
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)
 
 
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    

    @app.route('/')
    def index():
        return render_template("home.html")

    
    @app.route('/home')
    def home():
        return render_template("home.html") 
    
    @app.route('/init-db')
    def init_db_handler():
        init_db()
        return "DB Initialized" 
        
     
    @app.route('/test')
    # @login_required
    def test():               
        return "Test Complete !!"

    
    from auth.api.Auth_Api import auth_api
    app.register_blueprint(auth_api, url_prefix='/auth')
     
    from masters.api.Payment_Details_Api import payment_details_api
    app.register_blueprint(payment_details_api, url_prefix='/payment-details')
    
    from masters.api.Company_Api import company_api
    app.register_blueprint(company_api, url_prefix='/company-setup')

    # from masters.api.Products_Services_Api import products_and_services_api
    # app.register_blueprint(products_and_services_api, url_prefix='/products-services')
    
    # from invoice.api.Invoice_Api import invoice_api
    # app.register_blueprint(invoice_api, url_prefix='/invoices')
    
    # from clients.api.Client_Api import client_api
    # app.register_blueprint(client_api, url_prefix='/clients')

    db.init_app(app)
    app.cli.add_command(init_db_command)


    app.config['SECRET_KEY'] = 'mysecretkey'
    # loginManager = LoginManager()
    loginManager.login_view = '/auth/login'

    loginManager.init_app(app)

    @app.errorhandler(404)
    def errorhandler(e):
        return render_template("error-handler/not-found-handler.html", error=e)
         
    return app


def init_db(): 
    
    print (db.get_binds())
    # db.drop_all()
    db.create_all() 


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
 

if __name__ == "__main__" : 
    print("\n\nStarting App!\n\n") 
    app = create_app()
    app.run(debug=True) 