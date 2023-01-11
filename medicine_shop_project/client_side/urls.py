from django.urls import path

from .views import MedicineListView, IndexView, MedicineDetailView, MedicineUpdate

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='medicines'),
    path('medicine/<slug:slug>', MedicineDetailView.as_view(),
         name='medicine_detail'),
    path('medicine/<slug:slug>/update/', MedicineUpdate.as_view(),
         name='update_medicine'),
    # path('cart/', MedicineOrderView.as_view(), name='order_medicine'),
    # path('make-order/', order_medicine()),
    path('', IndexView.as_view(), name='home'),
]
