from faker import Faker
import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoodMart.settings")
import django
django.setup()
from django.core.management import call_command
from accounts.models import Account
from django.db.utils import IntegrityError
fake = Faker()

def generate_fake_account(gen_for, number):
    for i in range(number):
        name = fake.name()
        email = '.'.join(name.lower().split()) + str(random.randint(1000, 9999)) + '@gmail.com'
        password = 'Demon9968!!'
        fname = name.split()[0]
        lname = name.split()[1]
        mobile = int('98134' + str(random.randint(10, 99)) + str(i))
        try:
            user = Account(first_name=fname, last_name=lname, username=name, email=email, phone_no=mobile)
        except django.db.utils.IntegrityError:
            email = '.'.join(name.lower().split()) + '.' + str(random.randint(1000, 9999)) + '@gmail.com'
            user = Account(first_name=fname, last_name=lname, username=name, email=email, phone_no=mobile)

        user.set_password(password)
        if gen_for == 'vendor':
            user.is_vendor = True
        else:
            user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        if gen_for == 'vendor':
            user.is_customer = False
        else:
            user.is_customer = True
        user.save()
        print(user.id)


generate_fake_account('customer', 999)
generate_fake_account('vendor', 101)

# generate_fake_vendor()