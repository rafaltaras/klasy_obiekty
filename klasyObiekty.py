from faker import Faker
fake = Faker()

class ksiazkaAdresowa():
    def __init__(self, imie, nazwisko, nazwa_firmy, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.adres_email = adres_email
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email}"

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email}"

wizytowka1 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka1)

wizytowka2 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka2)

wizytowka3 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka3)

wizytowki = [wizytowka1, wizytowka2, wizytowka3]
print(wizytowki)
print("")
by_name = sorted(wizytowki, key=lambda wizytowka: wizytowka.imie)
print(by_name)
by_lastname = sorted(wizytowki, key=lambda wizytowka: wizytowka.nazwisko)
print(by_lastname)
by_email = sorted(wizytowki, key=lambda wizytowka: wizytowka.adres_email)
print(by_email)


