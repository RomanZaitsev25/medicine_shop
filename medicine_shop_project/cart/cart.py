# from decimal import Decimal
# from django.conf import settings
# from ..client_side.models import MedicineOrder
#
#
# class Cart(object):
#
#     def __init__(self, request):
#         """
#         Инициализируем корзину
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # save an empty cart in the session
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#     def add(self, medicine, quantity=1, update_quantity=False):
#         """
#         Добавить продукт в корзину или обновить его количество.
#         """
#         medicine_id = str(medicine.id)
#         if medicine_id not in self.cart:
#             self.cart[medicine_id] = {'quantity': 0,
#                                      'price': str(medicine.price)}
#         if update_quantity:
#             self.cart[medicine_id]['quantity'] = quantity
#         else:
#             self.cart[medicine_id]['quantity'] += quantity
#         self.save()
#
#     def save(self):
#         # Обновление сессии cart
#         self.session[settings.CART_SESSION_ID] = self.cart
#         # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
#         self.session.modified = True
#
#     def remove(self, medicine):
#         medicine_id = str(medicine.id)
#         if medicine_id in self.cart:
#             del self.cart[medicine_id]
#             self.save()
#
#     def __iter__(self):
#         """
#         Перебор элементов в корзине и получение продуктов из базы данных.
#         """
#         medicine_ids = self.cart.keys()
#         # получение объектов product и добавление их в корзину
#         medicines = MedicineOrder.objects.filter(id__in=medicine_ids)
#         for medicine in medicines:
#             self.cart[str(medicine.id)]['product'] = medicine
#
#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item
#
#     def __len__(self):
#         """
#         Подсчет всех товаров в корзине.
#         """
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         """
#         Подсчет стоимости товаров в корзине.
#         """
#         return sum(Decimal(item['price']) * item['quantity'] for item in
#                    self.cart.values())
#
#     def clear(self):
#         # удаление корзины из сессии
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True