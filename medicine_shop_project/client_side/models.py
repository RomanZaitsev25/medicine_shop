from django.db import models
from django.urls import reverse

from medicine_shop_project.staff_side.models import Staff


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    legacy_name = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)  # ForeignKey to Country
    legacy_address = models.CharField(max_length=250)

    # contacts
    site = models.URLField()
    contacts = models.CharField(max_length=250)
    email = models.EmailField()


class Medicine(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    trade_name = models.CharField(max_length=250, unique=True)
    international_name = models.CharField(max_length=250, unique=True)
    structure = models.TextField(default='Состав лекарства')
    price = models.FloatField(default=0.0)
    manufacturer = models.TextField()  # ManyToMany to Manufacturer
    slug = models.SlugField(default='', unique=True)
    _price_increment = models.IntegerField()

    @property  # получение значения защищенного поля
    def price_increment(self):
        return self._price_increment

    @price_increment.setter  # изменение значения защищенного поля
    def price_increment(self, value):
        if value > 10:
            raise Exception("Негодно к продаже!")  # это временная валидация
        else:
            self._price_increment = value
            self.save()

    class Meta:
        ordering = ["-the_cost_of_the_medicines"]
        unique_together = [["trade_name", "international_name"]]  # взаимоуникальные значения

    def get_absolute_url(self):
        return reverse('medicine_details', args=[self.slug])

    def __str__(self):
        return self.trade_name


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    receive_date_time = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    delivery_date_time = models.DateTimeField(verbose_name='Дата выдачи заказа', null=True)
    cost = models.FloatField(verbose_name='Стоимость', default=0.0)
    complete = models.BooleanField(verbose_name='Готовность заказа', default=False)

    staff = models.ForeignKey(Staff, verbose_name='Сотрудник', on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, verbose_name='Лекарства', through='MedicineOrder')


class MedicineOrder(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    amount = models.IntegerField(default=1)
