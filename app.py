from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
 
app = Flask(__name__)
Bootstrap(app) 
FontAwesome(app)
 
@app.route('/')
def index():
    return render_template("home.html")

 
@app.route('/home')
def home():
    return render_template("home.html") 

  
from auth.api.Auth_Api import auth_api
app.register_blueprint(auth_api, url_prefix='/auth')
  
from products.api.Products_Api import products_api
app.register_blueprint(products_api, url_prefix='/products-services')


@app.errorhandler(404)
def errorhandler(e):
    return render_template("error-handler/not-found-handler.html", error=e)
        

if __name__ == "__main__" : 
    app.run(debug=True)
 
