import re
import string
from pathlib import Path

from tinydb import TinyDB


class User:
    DB = TinyDB(Path(__file__).parent / "db.json", indent=4)

    def __init__(self, first_name, last_name, phone_number="", address=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"User(first_name={self.first_name})"

    def __str__(self):
        return f"{self.full_name}\nTél: {self.phone_number}\n{self.address}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def _check_user(self):
        self._check_full_name()
        self._check_phone_number()

    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Numéro de téléphone invalide: {self.phone_number}")

    def _check_full_name(self):
        if not (self.first_name and self.last_name):
            raise ValueError(f"Prénom et nom ne peuvent pas être vides : {self.first_name} {self.last_name}")

        special_characters = string.punctuation + string.digits
        if any(char in special_characters for char in self.first_name + self.last_name):
            raise ValueError(f"Prénom et nom ne peuvent pas contenir de caractères spéciaux : {self.first_name} {self.last_name}")

    def save(self, validate_data=False):
        if validate_data:
            self._check_user()
        return User.DB.insert(self.__dict__)



if __name__ == '__main__':
    from faker import Faker
    fake = Faker(locale="fr_FR")
    print("-" * 80)
    for _ in range(10):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    address=fake.address())

        user.save()
        print(user)
        print("-" * 80)