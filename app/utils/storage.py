import logging

from firebase_admin import (
    credentials,
    initialize_app,
    storage
)

from app.enums.Environments import Environment

logger = logging.getLogger(__name__)


class Firebase:
    _instance = None

    def __init__(self):
        self.__valid_layers = ["bronze", "silver", "gold"]

        credentials_json = {
            "type":
                str(Environment.TYPE),
            "project_id":
                str(Environment.PROJECT_ID),
            "private_key_id":
                str(Environment.PRIVATE_KEY_ID),
            "private_key":
                str(Environment.PRIVATE_KEY)
                .replace('\\n', '\n'),
            "client_email":
                str(Environment.CLIENT_EMAIL),
            "client_id":
                str(Environment.CLIENT_ID),
            "auth_uri":
                str(Environment.AUTH_URI),
            "token_uri":
                str(Environment.TOKEN_URI),
            "auth_provider_x509_cert_url":
                str(Environment.AUTH_PROVIDER_X509_URL),
            "client_x509_cert_url":
                str(Environment.CLIENT_X509_CERT_URL),
            "universe_domain":
                str(Environment.UNIVERSE_DOMAIN),
        }

        cred = credentials.Certificate(credentials_json)
        self.firebase = (
            initialize_app(cred,
                           {
                               'storageBucket': str(Environment.BUCKET)
                           }))

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def upload_file(self, file_name, file_path, layer="bronze"):
        logger.info('uploading file {}'.format(file_name))

        if layer not in self.__valid_layers:
            raise ValueError("Invalid layer. Must be one of: "
                             "bronze, silver, gold")
        bucket = storage.bucket()

        storage_path = f"{layer}/{file_name}"

        bucket.blob(storage_path).upload_from_filename(file_path)

        logger.info('uploaded file {} on bucket {}'
                    .format(file_name, storage_path))
