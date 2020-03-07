import os
import urllib.parse 

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy ()

loginManager = LoginManager()


ENVIRONMENT = os.environ['PY_ENVIRONMENT']

# Get environment variables  
DB_SERVER = os.environ['PY_FLASK_DB_SERVER']
DB_USERNAME = os.environ['PY_FLASK_DB_USERNAME']
DB_PASSWORD = os.environ['PY_FLASK_DB_PASSWORD']
DB_NAME = os.environ['PY_FLASK_DB_NAME']


def config_init_db  ( app ):  
    if ENVIRONMENT.lower() == "Dev".lower() :
        config_init_db_mssql ( app )  
    elif ENVIRONMENT.lower() == "Test".lower() :
        config_init_db_mssql ( app)  
    elif ENVIRONMENT.lower() == "Prod".lower() :
        config_init_db_mssql ( app ) 

 
def config_init_db_mssql( app ):   
    db_driver = ''

    if ENVIRONMENT.lower() == "Dev".lower() :
        db_driver = '{SQL Server}' 
    elif ENVIRONMENT.lower() == "Test".lower() :
        db_driver = '/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.2.1'  
    elif ENVIRONMENT.lower() == "Prod".lower() :
        db_driver = '{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.2.1}' 
   

    # Configure Database URI: DB_SERVER, DB_NAME, DB_USERNAME, DB_PASSWORD 
    params = urllib.parse.quote_plus( "DRIVER={" + db_driver + "};" + f"SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD}" )
 
    # initialization 
    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    # extensions
    global db
    db = SQLAlchemy(app) 

    print ('\n\n\n\n')
    print ('Environment Variables Initialised with below values')
    print( db_driver, "; ", DB_SERVER, "; ", DB_NAME, "; ", DB_USERNAME, "; ", DB_PASSWORD )
    print ("ENVIRONMENT :", ENVIRONMENT)
    print ("\n\n\n\n")


# def config_db_settings_sqlite(app):    
#     global db

#     basedir = os.path.abspath(os.path.dirname(__file__)) 

#     app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
#     db = SQLAlchemy(app)
