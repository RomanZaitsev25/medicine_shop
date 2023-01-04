from datetime import datetime

# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from .filters import MedicineFilter
from .models import Medicine


class MedicineListView(ListView):
    """List of products must be here. Use it properly."""

    model = Medicine
    template_name = 'medicine.html'
    context_object_name = 'medicines'
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MedicineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        return context


class MedicineDetailView(DetailView):
    # permission_required = ('my_farmasy.view_medicine',)  # <--- тут запятую забыл после пермишена:
    # у тебя разрешения передаются в виде кортежа, а не строки
    model = Medicine
    template_name = 'one_medicine.html'
    context_object_name = 'medicine'

    def get_object(self, **kwargs):
        return get_object_or_404(Medicine, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Детальная страница лекарства'
        context['time_now'] = datetime.utcnow()
        context['is_admin'] = self.request.user.groups.filter(
            name='local_admin').exists()
        return context
