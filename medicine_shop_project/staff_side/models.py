from django.db import models


class Staff(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    age = models.IntegerField(null=True)
    salary = models.FloatField(default=0.0)
    vacations = models.IntegerField(default=25)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f"{self.first_name} - {self.second_name} - {self.position=}" \
               f" - {self.age=} - {self.salary=}$" \
               f"-{self.vacations}"
