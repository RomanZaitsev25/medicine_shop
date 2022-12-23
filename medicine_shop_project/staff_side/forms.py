from django import forms
from django.core.exceptions import ValidationError
from .models import Staff


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ['first_name', 'second_name', 'age', 'schedule_type',
                  'background', 'position',  'salary', 'vacations']

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 14:
            raise ValidationError("Недопустимый возраст")

        else:
            if 14 < age < 18:
                raise ValidationError(
                    "Требуется письменное согласие родителей!"
                )
        return age

