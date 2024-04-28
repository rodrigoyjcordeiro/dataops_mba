from steps.abstract.abstract_step import Step
from utils.generete_file_name import (generate_data_file_name_silver,
                                      generate_metadata_file_name,
                                      generate_data_file_name_bronze)
from utils.mongo import MongoDBConnector

from utils.storage import Firebase

import logging
import os
import datetime

logger = logging.getLogger(__name__)


class StorageSender(Step):
    def __init__(self):
        self.firebase = Firebase()
        self.__valid_layers = ["bronze", "silver", "gold"]

    def exec(self, **kwargs):
        self.send_bronze_data_file()
        self.send_silver_data_file()
        self.send_dictionary()
        self.delete_temp_files()

    def send_bronze_data_file(self):
        file_name = generate_data_file_name_bronze()

        try:
            self.firebase.upload_file(
                file_name=file_name,
                file_path="universidades.csv",
                layer="bronze"
            )

            self.__save_log(file_name=file_name, upload_status=True)
        except Exception as e:
            logger.error(e)
            self.__save_log(file_name=file_name, upload_status=False, error=e)

    def send_silver_data_file(self):
        file_name = generate_data_file_name_silver()

        try:
            self.firebase.upload_file(
                file_name=file_name,
                file_path="dados.csv",
                layer="silver"
            )

            self.__save_log(
                file_name=file_name,
                upload_status=True
            )

            logger.info(
                'uploaded file {} successfully'
                .format(file_name)
            )

        except Exception as e:
            logger.error(e)
            self.__save_log(
                file_name=file_name,
                upload_status=False,
                error=e
            )

    def send_dictionary(self):
        file_name = generate_metadata_file_name()

        try:
            self.firebase.upload_file(
                file_name=file_name,
                file_path="dicionario.csv",
                layer="silver"
            )

            self.__save_log(
                file_name=file_name,
                upload_status=True
            )

        except Exception as e:
            logger.error(e)
            self.__save_log(
                file_name=file_name,
                upload_status=False,
                error=e
            )

    def delete_temp_files(self):
        try:
            logger.info('deleting temp files')
            os.remove("dados.csv")
            os.remove("dicionario.csv")
            os.remove("universidades.csv")
            logger.info("Temporary files removed successfully")
        except Exception as e:
            logger.error(f"Error deleting temporary files: {e}")

    def __save_log(self, file_name, upload_status, error=None):
        mongo = MongoDBConnector()

        if upload_status:
            logger.info('saving success log')
        else:
            logger.info('saving failure log')

        data = {
            "file_name": file_name,
            "insert_date": datetime.datetime.now(),
            "status_upload": upload_status,
            "error": error
        }

        mongo.insert(data)
        logger.info("Log saved successfully")
