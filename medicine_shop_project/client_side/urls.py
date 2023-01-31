from django.urls import path

from .views import MedicineListView, IndexView, MedicineDetailView, \
    add_to_cart, cart_view, RegisterUser, LoginUser, logout_user, \
    ContactFormView, cart_remove

urlpatterns = [
    path('medicine/', MedicineListView.as_view(), name='medicines'),
    path('medicine/<slug:slug>', MedicineDetailView.as_view(),
         name='medicine_detail'),
    path('medicine/<int:pk>/add_to_cart/', add_to_cart,
         name='add_to_cart'),

    path('medicine/cart_remove/', cart_remove,
         name='cart_remove'),

    path('cart/<slug:user_id>', cart_view, name='cart'),
    path('', IndexView.as_view(), name='home'),
    # path('register/', Register.as_view(), name='register'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]
