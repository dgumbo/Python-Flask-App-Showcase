import os
import urllib.parse 

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

loginManager = LoginManager()


def config_db_settings_sqlite(app):    
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)

from sqlalchemy import create_engine


def config_init_db_mssql(app):       
    db_server="denzil-test.database.windows.net"
    db_username="denzil"
    db_password="Password1"
    db_name = "python-flask-test" 
    db_driver = '{SQL Server}' 

    # Configure Database URI: 
    params = urllib.parse.quote_plus(f"DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};UID={db_username};PWD={db_password}")
 
    # initialization 
    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    # extensions
    db = SQLAlchemy(app)