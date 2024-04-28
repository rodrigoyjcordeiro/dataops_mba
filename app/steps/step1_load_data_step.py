import json
import logging

import requests

from app.enums.Environments import Environment
from app.steps.abstract.abstract_step import Step

logger = logging.getLogger(__name__)


class LoadData(Step):
    def exec(self, **kwargs):
        """
        loads universities data from api
        """
        logger.info('getting universities')
        url = Environment.API_UNIVERSITIES.value
        response = requests.get(url)

        if response.status_code == 200:
            logger.info('universities was loaded')
            return json.loads(response.content)
        else:
            (logger
             .error("Error while requesting "
                    "data universities:",
                    response.status_code))
