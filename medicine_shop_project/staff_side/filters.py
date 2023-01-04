from django_filters import FilterSet

from .models import Staff


class StaffFilter(FilterSet):

    class Meta:
        model = Staff
        fields = {
            'first_name': ['icontains'],
            'second_name': ['icontains'],
            'date_of_birth':  [
                'lte',
                'gte',
            ],
            '_salary': [
                'lt',
                'gt',
            ],
        }
