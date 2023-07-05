from dz36_order_payment_system import Order
from dz36_product_storage_suppliers import Product


class Employee:
    def __init__(self, name, salary, bonus, occupation):
        self.name = name
        self.__salary = salary
        self.__bonus = bonus
        self.occupation = occupation


class OnlineSupport(Employee):
    pass


class OrderPickers(Employee):
    orders_in_work = []

    def prepare_order(self, order):
        if order.status == "Paid":
           self.orders_in_work.append(order)
        else:
            pass

    def send_order_to_packer(self):
        if product1.check_product_in_storage == "Product will be delivery from storage":
           return f'{order1.id} for packer'
        else:
            return f'No orders'


class Packers(Employee):
    def __init__(self, name, salary, bonus, occupation):
        super().__init__(name, salary, bonus, occupation)
        self.order_to_shipping = None

    def send_order_to_shipping(self, send_order_to_packer):
        self.order_to_shipping = send_order_to_packer()

# order1 = Order(1, "MP1W0", 2000, "UApost")
# product1 = Product(order1.article)

