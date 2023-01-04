from django_filters import FilterSet

from .models import Staff


class StaffFilter(FilterSet):

    class Meta:
        model = Staff
        fields = {
            'name': ['icontains'],
            'age':  [
                'lt',
                'gt',
            ],
            'salary': [
                'lt',
                'gt',
            ],
        }
