from django.db.models.signals import post_init
from django.dispatch import receiver
from .models import Order, MedicineOrder, MedicineCart, Cart


@receiver(post_init, sender=Order)
def set_total_cost_order(sender, instance, **kwargs):
    instance.cost = 0
    medicines = MedicineOrder.objects.filter(order__id=instance.id)
    for medicine in medicines:
        instance.cost += medicine.get_total_medicine_cost()


@receiver(post_init, sender=Cart)
def set_total_cost_order(sender, instance, **kwargs):
    instance.cost = 0
    medicines = MedicineCart.objects.filter(cart__id=instance.id)
    for medicine in medicines:
        instance.cost += medicine.get_total_medicine_cost()
