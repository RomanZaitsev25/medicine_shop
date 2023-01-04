import datetime
import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Order, Medicine, Manufacturer


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ['trade_name', 'international_name', 'structure',
                  'price', 'manufacturer', 'amount_on_stock', '_price_increment',
                  'with_recipe', 'slug']
        widgets = {
            'structure': forms.Textarea(attrs={'cols': 60, 'rows': 7}),
            'with_recipe': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть меньше нуля')
        return price

    # Не работает валидация о недопустимых символах
    def clean_trade_name(self):
        trade_name = self.cleaned_data['trade_name']
        pattern = re.compile(r'[.,?:%^&*!]')
        if pattern.findall(trade_name):
            raise ValidationError('Недопустимые символы')
        return trade_name


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['delivery_date_time', 'complete']

    def clean_delivery_date_time(self):
        delivery_date_time = self.cleaned_data['delivery_date_time']
        if delivery_date_time is not None and delivery_date_time.replace(tzinfo=None) < datetime.datetime.utcnow():
            raise ValidationError('Дата доставки не может быть меньше даты принятия заказа!')
        return delivery_date_time


class ManufacturerForms(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'

    def clean_contacts(self):
        contacts = self.cleaned_data['contacts']
        pattern = re.compile(r'[.,?:%^&*!]')
        if pattern.findall(contacts):
            raise ValidationError('Недопустимые символы')
        return contacts
