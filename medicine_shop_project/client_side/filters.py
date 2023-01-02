from django_filters import FilterSet
from .models import Medicine


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class MedicineFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Medicine
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'trade_name': ['icontains'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }
