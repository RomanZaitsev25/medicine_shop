from datetime import datetime

from django.views.generic import ListView, TemplateView

from .filters import MedicineFilter
from .models import Medicine


class MedicineListView(ListView):
    """List of products must be here. Use it properly."""

    model = Medicine
    template_name = 'products.html'
    context_object_name = 'products'
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
