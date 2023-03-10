from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Staff
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def used_new_user(sender, instance, created, **kwargs):
    if created:
        print(f'Пользователь {instance.username} создан')
    else:
        print(f'Пользователь{instance.username} обновлён')


@receiver(post_save, sender=Staff)
def used_new_staff(sender, instance, **kwargs):
    created = kwargs['created']
    if created:
        print(f'Создан  сотрудник {instance.first_name}')
    else:
        print(f'Добавлены изменения к сотруднику {instance.first_name}')


@receiver(post_delete,  sender=Staff)
def delete_staff(sender, using, instance, **kwargs):
    print(f" Сотрудник {instance.first_name} уволен")
