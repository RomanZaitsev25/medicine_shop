from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import Order, Medicine, Country, Manufacturer, MedicineOrder, MedicineManufacturer
from .forms import MedicineForm, ManufacturerForms, OrderForm


class MedicineManufacturerInline(admin.TabularInline):
    model = MedicineManufacturer
    verbose_name = 'Производитель лекарств'
    verbose_name_plural = 'Производители лекарств'
    extra = 1


class MedicineOrderInline(admin.TabularInline):
    model = MedicineOrder
    verbose_name = 'Лекарство на заказ'
    verbose_name_plural = 'Лекарства на заказ'
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (MedicineOrderInline,)
    list_display = ('receive_date_time', 'delivery_date_time', 'cost', 'complete')
    list_filter = ('receive_date_time', 'delivery_date_time', 'cost', 'complete')
    search_fields = ('receive_date_time', 'delivery_date_time', 'cost', 'complete')
    form = OrderForm


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    inlines = (MedicineManufacturerInline,)
    list_display = ('trade_name', 'price', 'amount_on_stock', 'with_recipe')
    list_filter = ('trade_name', 'price', 'with_recipe')
    search_fields = ('trade_name', 'price', 'with_recipe')
    form = MedicineForm
    save_on_top = True
    fieldsets = (
        ('Общие данные', {
            'fields': (
                'trade_name',
                'international_name',
                'price',
                'structure',
                'amount_on_stock',
                'with_recipe',
            )
        }),
        ('Дополнительные данные', {
            'fields': ('_price_increment',  'slug')
        }),
    )

    # def image_show(self, obj):
    #     if obj.image:
    #         return mark_safe("<img src='{}' width = '60'/>"
    #                          ".format(obj.image.url)")
    #     return "None"
    # image_show.__name__ = "Картинка"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_country')
    list_filter = ('name_country',)
    search_fields = ('name_country',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'legacy_name', 'country', 'site')
    list_filter = ('legacy_name', 'country', 'site')
    search_fields = ('legacy_name', 'country', 'site')
    form = ManufacturerForms
