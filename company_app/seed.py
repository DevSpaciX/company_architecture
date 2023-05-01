from django.contrib.auth.models import User
from company_app.models import Employee
from django_seed import Seed


# seeder = Seed.seeder()
# # seeder.add_entity(Employee, 50)
#
# from faker import Faker
# fake = Faker()
#
# seeder.add_entity(Employee, 10, {
#     'name': lambda x: fake.name(),
#     'position': lambda x: fake.job(),
#     'hire_date': '2022-01-01',
#     'email': lambda x: fake.email(),
# })