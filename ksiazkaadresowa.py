from faker import Faker
fake = Faker()


class BaseContact():
    def __init__(self, first_name, last_name, company_phone, address_email):
        self.first_name = first_name
        self.last_name = last_name
        self.company_phone = company_phone
        self.address_email = address_email

    # def __str__(self):
    #     return f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.company_phone} {self.address_email}"

    def basecontact(self):
        return f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_lenght(self):
        return len(self.first_name) + len(str(" ")) + len(self.last_name)
 
class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.business_phone = business_phone
    
        self._contact = f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"
        
    def businesscontact(self):
        return f"{self.first_name} {self.last_name} {self.position} {self.company_name}"

def create_contacts(contact_type, quantity):
    results = []
    for i in range (0, quantity):
        if contact_type == "base":
            card = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email())
            # cards = card.basecontact
            results.append(card)
        elif contact_type == "business":
            card = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email(), position=fake.job(), company_name=fake.company(), business_phone=fake.phone_number() )
            # cards = card.businesscontact
            results.append(card.businesscontact())
    for i in results:
        print(i)

business_card1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email())
business_card2 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company_phone=fake.msisdn(), address_email=fake.email(), position=fake.job(), company_name=fake.company(), business_phone=fake.phone_number() )

print (business_card1.basecontact())
print (business_card1.label_lenght)
print (business_card2.basecontact())
print (business_card2.label_lenght)
# print('')
# print("Wizytówki base")
# create_contacts(contact_type='base', quantity=5)
print('')
print("Wizytówki bussines")
create_contacts(contact_type='business', quantity=2)



