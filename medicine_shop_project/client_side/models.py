from django.db import models
from django.urls import reverse


class Country(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name_country = models.CharField(
        verbose_name="Название страны",
        max_length=250,
        unique=True,
    )

    def __str__(self):
        return f"{self.name_country}"

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    legacy_name = models.CharField(
        verbose_name='Название организации',
        max_length=250,
        unique=True,
    )
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        on_delete=models.CASCADE,
    )
    legacy_address = models.CharField(verbose_name='Адрес', max_length=250)
    # contacts
    site = models.URLField(verbose_name='Сайт', blank=True, null=True)
    contacts = models.CharField(verbose_name='Контакты', max_length=250)
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True)

    def __str__(self):
        return f"{self.legacy_name} - {self.country}"

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Medicine(models.Model):
    DRUG_IMPLEMENTATION = [
        ('on medical prescription', 'по рецепту'),
        ('without medical prescription', 'без рецепта' )
    ]
    id = models.AutoField(primary_key=True, unique=True)
    trade_name = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        unique=True,
    )
    international_name = models.CharField(
        verbose_name='Международное название',
        max_length=250,
        unique=True,
    )
    structure = models.TextField(verbose_name='Состав', default='Состав лекарства')
    price = models.FloatField(verbose_name='Цена', default=0.0)
    manufacturer = models.ManyToManyField(
        Manufacturer,
        verbose_name='Производитель',
        through='MedicineManufacturer'
    )
    slug = models.SlugField(default='', unique=True)
    _price_increment = models.IntegerField(verbose_name='Наценка')
    sale_of_medicines = models.CharField(verbose_name='продажа лекарства',
                                         max_length=250,
                                         choices=DRUG_IMPLEMENTATION,
                                         default='on medical prescription')

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
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'
        ordering = ["-price"]
        unique_together = [["trade_name", "international_name"]]  # взаимоуникальные значения

    def get_absolute_url(self):
        return reverse('medicine_details', args=[self.slug])

    def __str__(self):
        return self.trade_name


class MedicineManufacturer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    medicine = models.ForeignKey(
        Medicine,
        verbose_name='Название лекарства',
        on_delete=models.CASCADE,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name='Производитель',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.medicine} - {self.manufacturer}"


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    receive_date_time = models.DateTimeField(
        verbose_name='Дата создания заказа',
        auto_now_add=True,
    )
    delivery_date_time = models.DateTimeField(
        verbose_name='Дата выдачи заказа',
        blank=True,
        null=True,
    )
    cost = models.FloatField(verbose_name='Стоимость', default=0.0)
    complete = models.BooleanField(verbose_name='Готовность заказа', default=False)
    medicines = models.ManyToManyField(
        Medicine,
        verbose_name='Лекарства',
        through='MedicineOrder',
    )

    def __str__(self):
        return f"{self.receive_date_time} - {self.delivery_date_time} : {self.cost} "

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class MedicineOrder(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.medicine} - {self.order}"
