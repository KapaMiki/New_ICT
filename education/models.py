from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError






STUDY_TYPES = (
    (0, ('Бакалавриат')),
    (1, ('Магистратура.')),
    (2, ('Докторантура')),
)

YEARS = (
    (1, ('1 курс.')),
    (2, ('2 курс')),
    (3, ('3 курс')),
    (4, ('4 курс')),
)



class Profession(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'



class Group(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    year = models.IntegerField(
        choices=YEARS, 
        default=0,
        verbose_name='Курс'
    )
    stude_type = models.IntegerField(
        choices=STUDY_TYPES, 
        default=0,
        verbose_name='Обучение'
    )
    proffesion = models.ForeignKey(
        Profession,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    