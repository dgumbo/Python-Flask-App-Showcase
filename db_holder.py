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


def config_init_db  (app):  

    if ENVIRONMENT.lower() == "Dev".lower() :
        config_init_db_mssql (app, DB_SERVER, DB_NAME, DB_USERNAME, DB_PASSWORD)
    elif ENVIRONMENT.lower() == "Test".lower() :
        config_init_db_mssql (app, DB_SERVER, DB_NAME, DB_USERNAME, DB_PASSWORD)
    elif ENVIRONMENT.lower() == "Prod".lower() :
        config_init_db_mssql (app, DB_SERVER, DB_NAME, DB_USERNAME, DB_PASSWORD)


# def config_db_settings_sqlite(app):    
#     global db

#     basedir = os.path.abspath(os.path.dirname(__file__)) 

#     app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
#     db = SQLAlchemy(app)



def config_init_db_mssql( app, db_server, db_name, db_username, db_password ):   
    # global db       

    # db_driver = '{SQL Server}' 
    # db_driver = 'ODBC Driver 13 for SQL Server'

    db_driver = '{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.4.so.2.1}'

    # Configure Database URI: 
    params = urllib.parse.quote_plus(f"DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};UID={db_username};PWD={db_password}")
 
    # initialization 
    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    # extensions
    global db
    db = SQLAlchemy(app) 

    print ('\n\n\n\n')
    print ('Environment Variables Initialised with below values')
    print( db_driver, "; ", db_server, "; ", db_name, "; ", db_username, "; ", db_password )
    print ("ENVIRONMENT :", ENVIRONMENT)
    print ("\n\n\n\n")