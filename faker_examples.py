from faker import Faker

fake = Faker(locale="ru_RU")

print(fake.email())
print(fake.first_name())
print(fake.address())