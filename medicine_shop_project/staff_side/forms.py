import datetime
from math import floor

from django import forms
from django.core.exceptions import ValidationError

from .models import Staff


class StaffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schedule_type'].empty_label = 'Категория не выбрана'
        self.fields['background'].empty_label = 'Категория не выбрана'
        self.fields['position'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Staff
        fields = ['first_name', 'second_name', 'sex', 'date_of_birth', 'schedule_type',
                  'background', 'position',  '_salary', 'vacations']
        # fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'vTextField'}),

        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data["date_of_birth"]
        age = floor((datetime.datetime.now().date() - date_of_birth).days / 365)
        if age < 14:
            raise ValidationError("Недопустимый возраст")
        else:
            if 14 < age < 18:
                raise ValidationError(
                    "Требуется письменное согласие родителей!"
                )
        return date_of_birth

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) > 250:
            raise ValidationError("Длинна превышает 250 символов")
        return first_name

    def clean_vacations(self):
        vacations = self.cleaned_data['vacations']
        if int(vacations) < 25:
            raise ValidationError("Отпуск не может быть меньше 25 дней")
        return vacations