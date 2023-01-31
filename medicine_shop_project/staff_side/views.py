from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .filters import StaffFilter
from .models import Staff


class ShowAllStaff(ListView):
    model = Staff
    template_name = 'my_all_staff.html'
    context_object_name = 'staffs'
    paginate_by = 3

    # # def get_queryset(self):
    # #     queryset = super().get_queryset()
    # #     self.filterset = StaffFilter(self.request.GET, queryset)
    # #     return self.filterset.qs
    #
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StaffFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_time'] = datetime.utcnow()
        context['title'] = 'Вторая страница'
        context['filterset'] = self.filterset
        return context


class ShowOneStaff(PermissionRequiredMixin, DetailView):
    model = Staff
    template_name = 'staff.html'
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вторая страница'
        context['is_admin'] = self.request.user.groups.filter(name='local_admin').exists()
        return context
