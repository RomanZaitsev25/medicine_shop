from django.db import models

# Create your models here.

from django.core.cache import cache
from django.db import models
from django.db import models
from django.urls import reverse

# Create your models here.


class Staff(models.Model):
    SCHEDULE_TYPE = [('FLEXIBLE', 'Flexible'), ('FULL_TIME', 'Full time')]
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    age = models.IntegerField(null=False)
    schedule_type = models.CharField(max_length=250, choices=SCHEDULE_TYPE, default='FULL_TIME')
    background = models.CharField(max_length=250)
    position = models.ForeignKey('Positions', on_delete=models.PROTECT)
    _salary = models.FloatField(default=0.0)
    vacations = models.IntegerField(default=25)


    def __str__(self):
        return f"Имя: {self.first_name} Фамилия: {self.second_name} Должность: {self.position}" \
               f"Возраст: {self.age} Зарплата: {self._salary}$" \
               f"Количество дней отпуска: {self.vacations}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
        self.save()


class Positions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    post_name = models.CharField(max_length=250)
    responsibility = models.CharField(max_length=1000)

    def __str__(self):
        return f" Позиция: {self.post_name} Обязанности: {self.responsibility}"
#
