from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
# from common.db.db_conn import db_connection  

# pip freeze > requirements.txt
 
app = Flask(__name__)
Bootstrap(app) 
FontAwesome(app)

# db = db_connection(app)

# from common.models.Base_Entity import BaseEntity

# baseE = BaseEntity()
# db.create_all()
 
@app.route('/')
def index():
    return render_template("home.html")

 
@app.route('/home')
def home():
    return render_template("home.html") 

  
from auth.api.Auth_Api import auth_api
app.register_blueprint(auth_api, url_prefix='/auth')
  
from masters.api.Products_Services_Api import products_and_services_api
app.register_blueprint(products_and_services_api, url_prefix='/products-services')
  
from masters.api.Company_Api import company_api
app.register_blueprint(company_api, url_prefix='/company-setup')
  
from masters.api.Payment_Details_Api import payment_details_api
app.register_blueprint(payment_details_api, url_prefix='/payment-details')
  
from invoice.api.Invoice_Api import invoice_api
app.register_blueprint(invoice_api, url_prefix='/invoices')
  
from clients.api.Client_Api import client_api
app.register_blueprint(client_api, url_prefix='/clients')


@app.errorhandler(404)
def errorhandler(e):
    return render_template("error-handler/not-found-handler.html", error=e)
        

if __name__ == "__main__" : 
    app.run(debug=True)
 
