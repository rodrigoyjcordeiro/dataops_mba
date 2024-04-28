import os
from enum import Enum


class Environment(Enum):
    API_UNIVERSITIES = os.getenv('API_UNIVERSITIES')
    TYPE = os.getenv('TYPE')
    PROJECT_ID = os.getenv('PROJECT_ID')
    PRIVATE_KEY_ID = os.getenv('PRIVATE_KEY_ID')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    CLIENT_EMAIL = os.getenv('CLIENT_EMAIL')
    CLIENT_ID = os.getenv('CLIENT_ID')
    AUTH_URI = os.getenv('AUTH_URI')
    TOKEN_URI = os.getenv('TOKEN_URI')
    AUTH_PROVIDER_X509_URL = os.getenv('AUTH_PROVIDER_X509_URL')
    CLIENT_X509_CERT_URL = os.getenv('CLIENT_X509_CERT_URL')
    UNIVERSE_DOMAIN = os.getenv('UNIVERSE_DOMAIN')
    MONGO_URI = os.getenv('MONGO_URI')
    BUCKET = os.getenv('BUCKET')

    def __str__(self):
        return self.value
