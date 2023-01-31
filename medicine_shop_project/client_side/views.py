from datetime import datetime
from decimal import Decimal

from django.contrib.auth import logout, login


from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, TemplateView, DetailView, \
    CreateView, FormView

from .filters import MedicineFilter
from .forms import RegisterUserForm, LoginUserForm, ContactForm, CartAddProductForm

from .models import Medicine, Cart, MedicineCart
from django.contrib.auth.mixins import LoginRequiredMixin
# menu = [{'title': 'обратная связь', 'url_name': 'contact'},
#         {'title': 'Войти', 'url_name': 'login'},
#         ]
# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def register(request):
#     return HttpResponse ('Регистрация')



# class Register(LoginRequiredMixin, CreateView):
#     form_class = MedicineAddForm
#     template_name = 'client_side/addpage.html'
#     login_url = reverse_lazy('home')
#     raise_exception = True
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Добавление ЛП'
#         return context



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'client_side/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Регистрация'
        return context

    # вызывается при успешной форме регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'client_side/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')



def logout_user(request):
    logout(request)
    return redirect('login')


# def register(request):
#     if request.method == 'POST':
#         # формируется заполненная форма
#         form = MedicineAddForm(request.POST)
#         # коректно ли заполнены данные и переданы на сервер
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('medicines')
#     else:
#         # формируем пустую форму
#         form = MedicineAddForm
#     return render (request, 'client_side/addpage.html', {'form': form})


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'client_side/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Обратная связь'
        return context

    # вызывается если пользователь заполнил все поля контактной формы
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')






class MedicineListView(ListView):
    model = Medicine
    template_name = 'client_side/medicine.html'
    context_object_name = 'medicines'
    allow_empty = False
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
    template_name = 'client_side/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['title'] = 'index'
        return context


class MedicineDetailView(DetailView):
    # permission_required = ('my_farmasy.view_medicine',)  # <--- тут запятую забыл после пермишена:
    # у тебя разрешения передаются в виде кортежа, а не строки
    model = Medicine
    template_name = 'client_side/one_medicine.html'
    context_object_name = 'medicine'

    def get_object(self, **kwargs):
        return get_object_or_404(Medicine, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Детальная страница лекарства'
        context['time_now'] = datetime.utcnow()
        # context['is_admin'] = self.request.user.groups.filter(
        #     name='local_admin').exists()
        return context


def cart_view(request, user_id):
    medicines_in_cart = MedicineCart.objects.filter(
        cart=Cart.objects.get(user__id=user_id)
    ).all()
    return render(
        request,
        template_name='client_side/cart.html',
        context={'medicines_in_cart': medicines_in_cart, 'title': 'cart'},
    )


def add_to_cart(request, pk):
    cart, created = Cart.objects.get_or_create(
        session_key=request.session.session_key,
        defaults={'user': request.user},
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


def cart_remove(request, medicine_id):
    # cart = CartAddProductForm(request.POST)
    cart = Cart(request)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    cart.remove(medicine)
    return redirect('medicine:medicine_detail')






# def cart_remove(request, medicine_id):
#     cart = Cart(request)
#     medicine = get_object_or_404(Medicine, id=medicine_id)
#     cart.delete(medicine)
#     return redirect('cart:cart_detail')

#
# def cart_remove(request, medicine_id):
#     medicine = get_object_or_404(MedicineCart, id=medicine_id)
#     medicine.delete()
#     return redirect('cart:cart_detail')
#
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'client_side/cart.html', {'cart': cart})


# @login_required(login_url='/login')
# def cart_checkout(request):
#     carts = Cart(request)
#     for cart in carts:
#         course = cart['course']
#         # course = get_object_or_404(Course, slug=course.slug)
#         Enroll.objects.create(course=course, user_id=request.user.id)
#     messages.success(request, 'Successfully checked out!')
#     carts.clear()
#     return redirect(reverse_lazy('cart:cart_detail'))






# def remove(self, medicine):
#     """
#     Удаление товара из корзины.
#     """
#     medicine_id = str(medicine.id)
#     if medicine_id in self.cart:
#         del self.cart[medicine_id]
#         self.save()

# def __len__(self):
#     """
#     Подсчет всех товаров в корзине.
#     """
#     return sum(item['quantity'] for item in self.cart.values())
#
#
# def get_total_price(self):
#     """
#     Подсчет стоимости товаров в корзине.
#     """
#     return sum(Decimal(item['price']) * item['quantity'] for item in
#                self.cart.values())
#
# def clear(self):
#     # удаление корзины из сессии
#     del self.session[settings.CART_SESSION_ID]
#     self.session.modified = True