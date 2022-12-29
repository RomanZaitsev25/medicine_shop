import datetime
from enum import Enum

from django.db import models
from django.template.defaultfilters import truncatechars


class Schedule(Enum):
    FLEXIBLE = "FLEXIBLE"
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"


class EducationCompleteness(Enum):
    FULL = "FULL"
    NOT_FULL = "NOT_FULL"


class Sex(Enum):
    MAN = 'M'
    WOMAN = 'W'


class Staff(models.Model):

    SCHEDULE_TYPE = [
        (Schedule.FLEXIBLE.value, 'Гибкий график'),
        (Schedule.FULL_TIME.value, 'Полный день'),
        (Schedule.PART_TIME.value, 'Частичная занятость'),
    ]
    SEX = [
        (Sex.MAN.value, 'Муж'),
        (Sex.WOMAN.value, 'Жен'),
    ]


    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    second_name = models.CharField(verbose_name='Фамилия', max_length=250)
    sex = models.CharField(max_length=1, verbose_name='Пол',
                           choices=SEX, default='M')
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        default=datetime.date(day=1, month=1, year=1970),
        null=False,
    )
    schedule_type = models.CharField(
        verbose_name='Расписание',
        max_length=250,
        choices=SCHEDULE_TYPE,
        default=Schedule.FULL_TIME.value,
    )
    background = models.ForeignKey('Backgrounds', verbose_name='Образование', on_delete=models.PROTECT)
    position = models.ForeignKey('Positions', verbose_name='Должность', on_delete=models.PROTECT)
    _salary = models.FloatField(verbose_name='ЗП, $', default=0.0)
    vacations = models.IntegerField(verbose_name='Дней отпуска', default=25)

    # отображение кнопки в админке

    def __str__(self):
        return f"Имя: {self.first_name}   Фамилия: {self.second_name}" \
               f" Должность: {self.position}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
        self.save()

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['second_name']


class Positions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    post_name = models.CharField(verbose_name='Должность', max_length=250)
    responsibility = models.CharField(verbose_name='Обязанности', max_length=1000)

    @property
    def short_description_responsibility(self):
        return truncatechars(self.responsibility, 35)

    def __str__(self):
        return f"{self.post_name} " \
               # f"\n Обязанности: {self.short_description_responsibility}"

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Backgrounds(models.Model):
    EDUCATION_COMPLETENESS = [
        (EducationCompleteness.FULL.value, 'Полное'),
        (EducationCompleteness.NOT_FULL.value, 'Неполное'),
    ]
    id = models.AutoField(primary_key=True, unique=True)
    educational_institution = models.CharField(verbose_name='Учебное заведение', max_length=250)
    education_completeness = models.CharField(
        verbose_name='Полнота образования',
        max_length=50,
        default=EducationCompleteness.FULL.value,
        choices=EDUCATION_COMPLETENESS,
    )

    def __str__(self):
        return f" Учебное заведение: {self.educational_institution}, " \
               f"{self.education_completeness}"

    class Meta:
        verbose_name = 'Уч. заведение'
        verbose_name_plural = 'Уч. заведения'
