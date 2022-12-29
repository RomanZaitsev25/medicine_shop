from django.contrib import admin

from .models import Order, Medicine, Country, Manufacturer, MedicineOrder, MedicineManufacturer


class MedicineManufacturerInline(admin.TabularInline):
    model = MedicineManufacturer
    verbose_name = 'Производитель лекарств'
    verbose_name_plural = 'Производители лекарств'
    extra = 1


class MedicineOrderInline(admin.TabularInline):
    model = MedicineOrder
    verbose_name = 'Лекарство на заказ'
    verbose_name_plural = 'Лекарства на заказ'
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (MedicineOrderInline,)
    list_display = ('receive_date_time', 'cost', 'complete')
    list_filter = ('receive_date_time', 'cost', 'complete')
    search_fields = ('receive_date_time', 'cost', 'complete')
    # form = OrderForm


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    inlines = (MedicineManufacturerInline,)
    list_display = ('trade_name', 'price')
    list_filter = ('trade_name', 'price')
    search_fields = ('trade_name', 'price')
    # form = MedicineForm


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
