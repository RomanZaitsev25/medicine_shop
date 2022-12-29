# Generated by Django 4.1.4 on 2022-12-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_side', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи заказа'),
        ),
    ]