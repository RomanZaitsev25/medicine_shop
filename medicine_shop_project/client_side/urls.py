from django.urls import path

from .views import MedicineListView, IndexView

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='products'),
    # path('medicine/<slug:slug>', MedicineDetailView.as_view(), name='product_details'),
    # path('cart/', MedicineOrderView.as_view(), name='order_medicine'),
    # path('make-order/', order_medicine()),
    path('', IndexView.as_view(), name='home'),
]
