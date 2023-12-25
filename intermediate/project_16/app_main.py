class User:
    def __init__(self, first_name, last_name, phone_number="", address=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}\nTél: {self.phone_number}\n{self.address}"


if __name__ == '__main__':
    from faker import Faker
    fake = Faker(locale="fr_FR")
    print("-" * 80)
    for _ in range(10):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    address=fake.address())

        print(user)
        print("-" * 80)