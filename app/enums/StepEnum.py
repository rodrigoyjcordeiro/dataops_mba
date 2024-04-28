from enum import Enum


class StepEnum(Enum):
    LOAD_DATA = ("loadData", "Etapa responsável pela carga de dados no sistema")
    PRUNING_DATA = ("pruningPhase", "Etapa responsável pela seleção dos dados pertinentes ao sistema")
    ALCHEMY_DATA = ("alchemyPhase", "Etapa responsável pela transformação dos dados em entidades do sistema")
    STORAGE_SENDER = ("storagePhase", "Etapa responsável pelo envio do arquivo ao Storage do firebase")

    def __str__(self):
        return self.value

    def __new__(cls, name, description):
        member = object.__new__(cls)
        member._value_ = name
        member.description = description
        return member
