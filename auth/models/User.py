from common.models.Base_Entity import BaseEntity 
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

from db_holder import db, loginManager

bcrypt = Bcrypt()

class User(BaseEntity, db.Model, UserMixin): 
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, nullable=False, index=True) 
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)  
    password_hash = db.Column(db.String(128), nullable=False)  

    # client_id = db.Column(db.Integer, db.ForeignKey('clients.id')) 
    
    invoices = db.relationship("Invoice", primaryjoin="User.id==Invoice.owner_id " )
    clients = db.relationship("Client", primaryjoin="User.id==Client.owner_id " )
    companies = db.relationship("Company", primaryjoin="User.id==Company.owner_id " )
    payment_details = db.relationship("PaymentDetail", primaryjoin="User.id==PaymentDetail.owner_id " )
    products = db.relationship("Product", primaryjoin="User.id==Product.owner_id " )
    services = db.relationship("Service", primaryjoin="User.id==Service.owner_id " )
    
    def __init__(self, username, email, password):
        BaseEntity.__init__(self)
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
