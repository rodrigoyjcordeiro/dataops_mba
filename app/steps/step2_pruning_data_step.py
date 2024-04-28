import logging

from steps.abstract.abstract_step import Step
import pandas as pd

logger = logging.getLogger(__name__)


class PruningData(Step):

    def exec(self, **kwargs):
        data = kwargs.get("data")
        df = pd.DataFrame(data)
        logger.info("filtering data columns")
        filtered_df = df[['name', 'country', 'web_pages']]
        logger.info("data columns filtered")
        return filtered_df
