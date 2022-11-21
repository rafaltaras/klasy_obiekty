from faker import Faker
fake = Faker()

class BaseContact():
    def __init__(self, first_name, last_name, company_phone, address_email):
        self.first_name = first_name
        self.last_name = last_name
        self.company_phone = company_phone
        self.address_email = address_email

        self._contact = f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}"

    def __len__(self):
        label_length = len(self.first_name) + len(self.last_name) + 1
        return label_length

 
class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.business_phone = business_phone
    
        self._contact = f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"


# def create_contacts(type, )

business_card1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email())
business_card2 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email(), position=fake.job(), company_name=fake.company(), business_phone=fake.phone_number() )

print(business_card1._contact)
print ("Długość imie + nazwisko to: ", len(business_card1))
print(business_card2._contact, len(business_card2))
print ("Długość imie + nazwisko to: ", len(business_card2))

