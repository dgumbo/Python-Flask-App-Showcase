from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
  
from db_holder import db

def CreateDBConn (app) -> SQLAlchemy:
    global db

    basedir = os.path.abspath(os.path.dirname(__file__)) 
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    return db
 
  

