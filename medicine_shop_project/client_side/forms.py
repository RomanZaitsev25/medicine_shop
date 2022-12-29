import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Order, Medicine, Manufacturer, MedicineManufacturer


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ['trade_name', 'international_name', 'structure',
                  'price', 'manufacturer', '_price_increment',
                  'sale_of_medicines']
        widgets = {
            'structure': forms.Textarea(attrs={'cols': 60, 'rows': 7})
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError(' Цена не может быть меньше нуля')
        return price

# Не работает валидация о недопустимых символах
    def clean_trade_name(self):
        trade_name = self.cleaned_data['trade_name']
        pattern = re.compile(r'[.,?:%^&*!]')
        if pattern.findall(trade_name):
            raise ValidationError('Недопустимые символы')
        return trade_name


# class OrderForm(forms.ModelForm):
#
#     class Meta:
#         model = Order
#         fields = ['receive_date_time', 'delivery_date_time', 'cost',
#                   'complete', 'medicines']
#
#     def clean_cost(self):
#         cost = self.cleaned_data['cost']
#         if cost < 0:
#             raise ValidationError(' Стоимость не может быть меньше нуля')
#         return cost

class ManufacturerForms(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'

    def clean_contacts(self):
        contacts = self.cleaned_data['contacts']
        pattern = re.compile(r'[.,?:%^&*!]')
        if pattern.findall(contacts):
            raise ValidationError('Не допустимые символы')
        return contacts

# не получилось
class MedicineManufacturerForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine'].empty_label = 'Лекарство не выбрана'

    class Meta:
        model = MedicineManufacturer
        fields = ['medicine', 'manufacturer']