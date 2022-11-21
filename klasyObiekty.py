from faker import Faker
fake = Faker()

class ksiazkaAdresowa():
    def __init__(self, imie, nazwisko, nazwa_firmy, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.adres_email = adres_email

        self._contact = f"Kontaktuje sie z  {self.imie} {self.nazwisko} {self.adres_email}"
        self._sumlen = 0

    def __len__(self):
        return  len(self.imie) + len(self.nazwisko) + 1
    
    # @property
    # def sumlen(self):
    #     return self._sumlen
    
    # @sumlen.setter
    # def sumlen(self):
    #     self._sumlen = len()
    #     return  self._sumlen

    # def __str__(self):
    #     return f"{self.imie} {self.nazwisko} {self.adres_email}"

    # def __repr__(self):
    #     return f"{self.imie} {self.nazwisko} {self.adres_email}"

wizytowka1 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka1._contact)
print(len(wizytowka1))

# wizytowka2 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
# print(wizytowka2)

# wizytowka3 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
# print(wizytowka3)


