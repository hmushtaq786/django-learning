import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')


import django

django.setup()

import random
from second_app.models import User
from faker import Faker

fakegen = Faker()

def add_user(N=10):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        t = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]
        t.save()
    
if __name__ == '__main__':
    print('Populating database...')
    add_user(20)
    print('Population completed!')