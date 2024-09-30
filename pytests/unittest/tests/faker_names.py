from faker import Faker

faker = Faker(locale="es_AR")

Faker.seed(0)

print(faker.name())
print(faker.phone_number())
print(faker.email())
