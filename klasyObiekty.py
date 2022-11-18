from faker import Faker
fake = Faker()

class ksiazkaAdresowa():
    def __init__(self, imie, nazwisko, nazwa_firmy, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.adres_email = adres_email

wizytowka = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka.imie, wizytowka.nazwisko, "pracuje w firmie:", wizytowka.nazwa_firmy, "i ma adres email:", wizytowka.adres_email)

wizytowka1 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka1.imie, wizytowka1.nazwisko, "pracuje w firmie:", wizytowka1.nazwa_firmy, "i ma adres email:", wizytowka1.adres_email)
    
wizytowka2 = ksiazkaAdresowa(imie=fake.first_name(), nazwisko=fake.last_name(), nazwa_firmy=fake.company(), adres_email=fake.email())
print(wizytowka2.imie, wizytowka2.nazwisko, "pracuje w firmie:", wizytowka2.nazwa_firmy, "i ma adres email:", wizytowka2.adres_email)

