from dz36_order_payment_system import Order


class Product:
    def __init__(self, article):
        self.article = article

    def check_product_in_storage(self):
        if dress.stock_of_product > 0:
            return f"Product is available"
        else:
            return f'Waiting from suppliers'


class Storage:
    def __init__(self, stock_of_product):
        self.stock_of_product = stock_of_product

    def take_product_from_suppliers(self, product):
        if dress.stock_of_product <= 0:
            return f"Product will be delivery from {supplier1.name} in 2 days"
        else:
            return f"Product will be delivery from storage"


class Suppliers:
    def __init__(self, name, product_type):
        self.name = name
        self.product_type = product_type


supplier1 = Suppliers("Fassion Salon", 'dress')
dress = Storage(0)
