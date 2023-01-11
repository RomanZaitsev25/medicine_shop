from django.urls import path

from .views import MedicineListView, IndexView, MedicineDetailView, add_to_cart, cart_view

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='medicines'),
    path('medicine/<slug:slug>', MedicineDetailView.as_view(),
         name='medicine_detail'),
    path('medicine/<int:pk>/add_to_cart/', add_to_cart,
         name='add_to_cart'),
    path('cart/<int:user_id>', cart_view, name='cart'),
    # path('make-order/', order_medicine()),
    path('', IndexView.as_view(), name='home'),
]
