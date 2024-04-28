from pymongo import MongoClient

from app.enums.Environments import Environment


class MongoDBConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super()\
                .__new__(cls, *args, **kwargs)
            cls._instance._client = MongoClient(
                str(Environment.MONGO_URI)
            )
            cls._instance._db = cls\
                ._instance._client['arquivos_ingestao_universidades']
            cls._instance._collection = cls\
                ._instance._db['historico_ingestao']
        return cls._instance

    def insert(self, dado):
        self._collection.insert_one(dado)

    def find(self, filtro):
        return self._collection.find_one(filtro)
