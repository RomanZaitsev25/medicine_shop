from datetime import datetime

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, TemplateView, DetailView, UpdateView

from .filters import MedicineFilter
from .models import Medicine, Cart, MedicineCart


class MedicineListView(ListView):
    """List of products must be here. Use it properly."""

    model = Medicine
    template_name = 'medicine.html'
    context_object_name = 'medicines'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MedicineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        context['title'] = 'medicines'
        return context


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['title'] = 'index'
        return context


def cart_view(request, user_id):
    medicines_in_cart = MedicineCart.objects.filter(
        cart=Cart.objects.get(user__id=user_id)
    ).all()
    return render(
        request,
        template_name='cart.html',
        context={'medicines_in_cart': medicines_in_cart, 'title': 'cart'},
    )


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


def add_to_cart(request, pk):
    if cart := Cart.objects.get(session_key=request.session.session_key):
        pass
    else:
        cart = Cart.objects.create(
            user=request.user,
            session_key=request.session.session_key,
        )

    try:
        MedicineCart.objects.create(
            medicine=Medicine.objects.get(id=pk),
            cart=cart,
        )
    except IntegrityError:
        medicine_cart = MedicineCart.objects.filter(
            medicine=Medicine.objects.get(id=pk),
            cart=cart,
        ).first()
        medicine_cart.amount += 1
        medicine_cart.save()
    return redirect(to='medicines')
