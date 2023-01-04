from django.urls import path

from .views import ShowAllStaff, ShowOneStaff

urlpatterns = [
    path('', ShowAllStaff.as_view(), name='staffs'),
    path('<int:pk>', ShowOneStaff.as_view(), name='staff'),

]