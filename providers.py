import logging
import os
from io import BytesIO

from faker import Faker
from PIL import Image

import random
import requests

import threading

fake = Faker()

payload = {}
path = "http://192.168.100.69:3000/providers"


def create_providers():
    images_list = os.listdir("media")
    image = random.choice(images_list)
    isIndividual = random.choice([True, False])
    password = fake.password()

    imageExtension = image.split(".")[-1]
    files = {
        "avatar": (image, open('media/' + image, 'rb'), f'image/{imageExtension}'),
        "isIndividual": (None, isIndividual),
        "companyName": (None, fake.company()),
        "user": (None,
                 '{"category": "INDIVIDUAL", "type": "CUSTOMER", "email": "' + fake.email() + '", "username": "' + fake.user_name() + '", "password": "' + password + '", "long": "' + str(
                     fake.longitude()) + '", "lat": "' + str(fake.latitude()) + '"}'),
        "phone": (None, fake.phone_number()),
        "hourlyRate": (None, "0"),
        "companyWebsiteUrl": (None, fake.url()),
        "vatNumber": (None, fake.ean8()),
        "country": (None, fake.country()),
        "postalCode": (None, fake.postcode()),
        "isOrganization": (None, not isIndividual)
    }

    session = requests.Session()
    print("Initiating the creation of provider")
    newResponse = session.post(path, files=files, json=payload)
    if newResponse.ok:
        print("Provider created")
        print(newResponse.json())
    else:
        print("Error creating provider")
        logging.error(newResponse.json())


def create_providers_threaded():
    for i in range(10):
        t = threading.Thread(target=create_providers)
        t.start()


def create_providers_threaded_threaded():
    for i in range(10):
        t = threading.Thread(target=create_providers_threaded)
        t.start()


for i in range(100):
    threading.Thread(target=create_providers_threaded_threaded).start()
