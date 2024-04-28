import logging

from steps.abstract.abstract_step import Step
import pandas as pd


logger = logging.getLogger(__name__)


class AlchemyData(Step):
    def exec(self, **kwargs):
        data = kwargs.get("data")
        data_df = pd.DataFrame(data)
        logger.info('applying alchemy_data step')
        data_df['name'] = data_df['name'].str.upper()
        data_df['country'] = data_df['country'].str.upper()
        data_df['country'] = data_df['country'].str.upper()
        data_df['web_pages'] = (data_df['web_pages']
                                .str.replace('http://', 'https://'))

        logger.info('applied alchemy_data step')

        try:
            logger.info('creating temp data file')
            data_df.to_csv('dados.csv', index=False)
            logger.info('temp data file created successfully')

            metadata = {
                'name': {
                    'descricao': 'Nome da universidade',
                    'tipo_tratamento': 'Uppercase',
                    'chave': True
                },
                'country': {
                    'descricao': 'País de origem',
                    'tipo_tratamento': 'Uppercase',
                    'chave': False
                },
                'web_pages': {
                    'descricao': 'Páginas na web',
                    'tipo_tratamento': 'adicionado https',
                    'chave': False
                }
            }

            df_info = (
                pd.DataFrame(metadata)
                .transpose()
                .reset_index()
            )

            df_info.columns = [
                'Nome do Campo',
                'Descricao',
                'tipo_tratamento',
                'chave'
            ]

            logger.info('creating temp metadata file')

            df_info.to_csv(
                'dicionario.csv',
                index=False
            )

            logger.info('temp metadata file created successfully')

            return True
        except Exception as e:
            logger.error(e)
            return False
