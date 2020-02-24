from common.models.Base_Entity import BaseEntity, db

class InvoiceLine(BaseEntity, db.Model): 
     
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False, index=True )
    
    service_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), index=True )
    product_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), index=True )

    quantity = db.Column(db.Integer, nullable=False )
    charge = db.Column(db.Integer, nullable=False )
    
    def __init__(self):
        BaseEntity.__init__(self)