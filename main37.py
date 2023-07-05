class AttributePrinterMixin:
    def __str__(self):
        return self.print_attributes()

    def print_attributes(self):
        attributes = vars(self)
        class_name = type(self).__name__
        attributes_str = ""
        for key, value in attributes.items():
            if key.startswith('_'):
                key_parts = key.split('__')
                key = key_parts[-1].lstrip('_')
                #   key = key[1:]
            attributes_str += f"\t{key}: {value}\n"
        return f"{class_name}: {{\n{attributes_str}}}"


class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

    def __str__(self):
        return super().__str__()


a = A()
print(a)
