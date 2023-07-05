class Order:
    def __init__(self, id, article, total_sum, shipping_method):
        self.id = id
        self.article = article
        self.__total_sum = total_sum
        self.shipping_method = shipping_method
        self.status = None


    def set_status(self, status):
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Article: {self.article}, Shipping Method: {self.shipping_method}, Status: {self.status}"

class PaymentSystem:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency

    def make_status(self, order):
        payment_successful = True

        if payment_successful:
            order.set_status("Paid")
        else:
            order.set_status("Waiting for payment")
