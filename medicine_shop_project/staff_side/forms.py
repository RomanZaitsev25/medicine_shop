import datetime
from math import floor

from django import forms
from django.core.exceptions import ValidationError
from .models import Staff


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ['first_name', 'second_name', 'date_of_birth', 'schedule_type',
                  'background', 'position',  '_salary', 'vacations']

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

