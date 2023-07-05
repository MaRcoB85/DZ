from dz36_order_payment_system import Order
from dz36_order_payment_system import PaymentSystem

from dz36_client import Client

from dz36_employee import OrderPickers
from dz36_employee import Packers

from dz36_product_storage_suppliers import Product
from dz36_product_storage_suppliers import Storage
from dz36_product_storage_suppliers import Suppliers

order1 = Order(1, "MP1W0", 2000, "UApost")
order2 = Order(2, "KI3VT", 1000, "UApost")
payment_system = PaymentSystem("Liqpay", "UAH")
payment_system.make_status(order1)
print(order1.status)    # payment status for order

client = Client("Maryna")
client.make_order("Dress")
client.make_order("Bag")
print(str(client))  # client's orders

order_picker1 = OrderPickers("Maryna", 3000, "None", "picker")
order1.set_status('Paid')
order_picker1.prepare_order(order1)
order2.set_status('Waiting')
order_picker1.prepare_order(order2)
print([str(order) for order in order_picker1.orders_in_work])  # which orders are in work (picker)

product1 = Product(order1.article)
product2 = Product(order2.article)

supplier1 = Suppliers("Fassion Salon", 'dress')
dress = Storage(0)
print(product1.check_product_in_storage())  # product is in storage or not?
print(dress.take_product_from_suppliers(product1)) # info about delivery from supplier

packer1 = Packers("Olga", 2000, "None", "packer")
print(order_picker1.send_order_to_packer())  # which orders are in work (packer)

print(packer1.order_to_shipping) # which orders go to the shipping company
