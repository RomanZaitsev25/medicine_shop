import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import Order, Medicine, Manufacturer


# class MedicineAddForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['with_recipe'].empty_label = 'Категория не выбрана'
#     # trade_name = forms.CharField(max_length=250,  widget=forms.TextInput(attrs={'class': 'form-input'}))
#     # international_name = forms.CharField(max_length=250)
#     # structure = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     # price = forms.FloatField()
#     # slug = forms.SlugField(max_length=250)
#     # _price_increment = forms.IntegerField()
#     # manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), label = 'Производитель', empty_label='Категория не выбрана')
#     # with_recipe = forms.BooleanField()
#     # amount_on_stock = forms.IntegerField()
#
#     class Meta:
#         model = Medicine
#         fields = ['trade_name', 'international_name', 'structure',
#                   'price', 'amount_on_stock', '_price_increment',
#                   'with_recipe', 'slug']
#
#         widgets = {
#             'structure': forms.Textarea(attrs={'cols': 60, 'rows': 7}),
#             'with_recipe': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#         }
#
#     def clean_name(self):
#         trade_name = self.cleaned_data['trade_name']
#         if len(trade_name) > 40:
#             raise ValidationError('Длинна названия ЛП превышает 40 символов')
#         return trade_name
#

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_password(self):
        password1 = self.cleaned_data['password1']
        pattern = re.compile(r'[.,?:%^&*!]')
        if pattern.findall(password1):
            raise ValidationError('Недопустимые символы')
        return password1

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()



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

    def clean_name(self):
        trade_name = self.cleaned_data['trade_name']
        if len(trade_name) > 200:
            raise ValidationError('Длинна названия ЛП превышает 200 символов')
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


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# quantity : позволяет пользователю выбрать количество между 1-20.
# update : позволяет указать, следует ли добавлять сумму к любому существующему
# значению в корзине для данного продукта (False) или если существующее
# значение должно быть обновлено с заданным значением (True).
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)