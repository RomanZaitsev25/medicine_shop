# from django.core.exceptions import ValidationError
# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# from ..client_side.models import Medicine
#
#
# class Cart(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=255, verbose_name='Key', unique=True)
#     cost = models.FloatField(verbose_name='Стоимость', default=0.0)
#     medicines = models.ManyToManyField(
#         Medicine,
#         verbose_name='Лекарства',
#         through='MedicineCart',
#     )
#
#     def __str__(self):
#         return f"{self.user} : {self.session_key}"
#
#     class Meta:
#         verbose_name = 'Корзина'
#         verbose_name_plural = 'Корзины'
#
#
# class MedicineCart(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     _amount = models.IntegerField(default=1)
#
#     def get_total_medicine_cost(self):
#         return self.medicine.price * self._amount
#
#     @property
#     def amount(self):
#         return self._amount
#
#     @amount.setter
#     def amount(self, value):
#         medicine = Medicine.objects.get(id=self.medicine.id)
#         if value > medicine.amount_on_stock:
#             raise Exception("На складе отсутствует данное количество товара!")
#         else:
#             self._amount = value
#             self.save()
#
#     def clean(self):
#         if self._amount > self.medicine.amount_on_stock:
#             raise ValidationError(
#                 "На складе отсутствует данное количество товара! "
#                 f"В данный момент на складе {self.medicine.amount_on_stock} ед."
#             )
#
#     def __str__(self):
#         return f"{self.medicine} - {self.cart}"
#
#     class Meta:
#         unique_together = [['medicine', 'cart']]

