from django.db import models


class TypeChoice(models.TextChoices):
    __empty__ = 'Выберите тип страницы'
    TXT = 'TXT', 'text'
    FRM = 'FRM', 'form'


class StatusChoice(models.TextChoices):
    __empty__ = 'Выберите статус товара'
    YES = 'YES', 'в наличии'
    LIM = 'LIM', 'количество ограничено'
    END = 'END', 'нет в наличии'
    ASK = 'ASK', 'под заказ'
    DEL = 'DEL', 'снято с производства'
