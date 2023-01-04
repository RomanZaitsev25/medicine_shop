from django.urls import path

from .views import MedicineListView, IndexView, MedicineDetailView

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='medicines'),
    path('medicine/<slug:slug>', MedicineDetailView.as_view(),
         name='medicine_detail'),
    # path('cart/', MedicineOrderView.as_view(), name='order_medicine'),
    # path('make-order/', order_medicine()),
    path('', IndexView.as_view(), name='home'),
]
