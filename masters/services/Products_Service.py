from masters.models.Product import Product
from masters.models.Service import Service
from common.service.Generic_Service import GenericService

class ProductsService(GenericService):

    def __init__(self):
        GenericService.__init__(self)

    def create_product(self, product):        
        return Product() #"Test User1", "Passwor1")
 
    def update_product(self, product, id):        
        return Product() #"Test User1", "Passwor1")
 
    def delete_product(self, product):        
        print (f"printing user on create user:  ") 
 
    def find_product(self, id):        
        return Product() #"Test User1", "Passwor1")

       
    def get_all_products(self) :
        products = []
        product1 = Product() #"Test User1", "Passwor1")
        product2 = Product() #"Test User2", "Passwor1")

        products.append(product1)
        products.append(product2)

        return products
        
       

    def create_service(self, service):        
        return Service() #"Test User1", "Passwor1")
 
    def update_service(self, service, id):        
        return Service() #"Test User1", "Passwor1")
 
    def delete_service(self, service):        
        print (f"printing user on create user:  ") 
 
    def find_service(self, id):        
        return Service() #"Test User1", "Passwor1")

    def get_all_services(self) :
        services = []
        service1 = Service() #"Test User1", "Passwor1")
        service2 = Service() #"Test User2", "Passwor1")

        services.append(service1)
        services.append(service2)

        return services