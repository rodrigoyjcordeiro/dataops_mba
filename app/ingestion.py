import logging

from app.enums.StepEnum import StepEnum
from app.steps.step1_load_data_step import LoadData
from app.steps.step3_alchemy_data_step import AlchemyData
from app.steps.step2_pruning_data_step import PruningData
from app.steps.step4_send_file_to_storage import StorageSender

logger = logging.getLogger(__name__)

steps = {
    "loadDataPhase": {
        "details": StepEnum.LOAD_DATA,
        "function": LoadData(),
    },
    "pruningPhase": {
        "details": StepEnum.PRUNING_DATA,
        "function": PruningData()
    },
    "alchemyPhase": {
        "details": StepEnum.ALCHEMY_DATA,
        "function": AlchemyData()
    },
    "SendEmailPhase": {
        "details": StepEnum.STORAGE_SENDER,
        "function": StorageSender()
    },
}


def run():
    res = None
    for phase, info in steps.items():
        logger.info(f"Nome da fase: {info['details'].name}")  # Correção aqui
        logger.info(f"Descrição da fase: "
                    f"{info['details'].value}")  # Adicionando descrição
        res = info['function'].exec(data=res)
