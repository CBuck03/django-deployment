import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_project.settings')

import django

django.setup()

## FAKE POPULATE SCRIPT
import random
from first_app.models import Topic, Webpage, AccessRecord, Users
from faker import Faker

fakegen = Faker()
topics = ['Life', 'Work', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def populate_users(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = f'{fake_first_name}.{fake_last_name}@mail.com'
        usrs = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print('populating script...')
    # populate(20)
    populate_users(20)
    print('populating complete!')
