from django.db import models


class TypeChoice(models.TextChoices):
    TXT = 'TXT', 'text'
    FRM = 'FRM', 'form'


class StatusChoice(models.TextChoices):
    YES = 'YES', 'в наличии'
    LIM = 'LIM', 'количество ограничено'
    END = 'END', 'нет в наличии'
    ASK = 'ASK', 'под заказ'
    DEL = 'DEL', 'снято с производства'
