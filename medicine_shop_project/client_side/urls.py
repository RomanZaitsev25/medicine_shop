from django.urls import path

from .views import MedicineListView, IndexView, ShowOneMedicineView

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='medicine'),
    path('medicine/<slug:slug>', ShowOneMedicineView.as_view(),
         name='one_medicine'),
    # path('cart/', MedicineOrderView.as_view(), name='order_medicine'),
    # path('make-order/', order_medicine()),
    path('', IndexView.as_view(), name='home'),
]
