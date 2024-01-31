class Laptop:
    discount = 10
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, string):
        import re
        item = re.findall('is \w*', string)
        name = item[0][3:]
        price = item[1][3:]
        return cls(name, int(price))

    def apply_discount(self):
        discount_amount = (self.price / 100) * self.discount
        final_amount = self.price - discount_amount
        return int(final_amount)

    def __str__(self):
        return f"{self.name} costs {self.price}"

    def __repr__(self):
        return f"{self.name} costs {self.price}"

