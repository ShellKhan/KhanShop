from enum import Enum


class TypeChoice(Enum):
    TXT = "text"
    FRM = "form"


class StatusChoice(Enum):
    YES = "в наличии"
    LIM = "количество ограничено"
    END = "нет в наличии"
    ASK = "под заказ"
    DEL = "снято с производства"
