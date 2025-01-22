from faker import Faker

fake = Faker()
fake_ru = Faker(locale='ru_RU')

def generate_login():
    return fake.word().capitalize() + str(fake.random_int(100, 999))

def generate_password():
    return fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

def generate_first_name():
    return fake_ru.first_name()
