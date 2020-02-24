from common.models.Base_Entity import BaseEntity, db
from invoice.models.Invoice_line import InvoiceLine

class Invoice(BaseEntity, db.Model): 
     
    invoice_date = db.Column(db.DateTime, nullable=False) 
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False, index=True )
    payment_detail_id = db.Column(db.Integer, db.ForeignKey('payment_detail.id'), nullable=False, index=True )
     
    invoice_lines = db.relationship(InvoiceLine, primaryjoin="Invoice.id==InvoiceLine.invoice_id " )

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True )
    
    def __init__(self):
        BaseEntity.__init__(self)

         