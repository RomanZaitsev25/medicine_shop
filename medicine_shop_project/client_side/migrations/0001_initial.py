# Generated by Django 4.1.2 on 2022-12-28 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_country', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('legacy_name', models.CharField(max_length=250, unique=True)),
                ('legacy_address', models.CharField(max_length=250)),
                ('site', models.URLField()),
                ('contacts', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client_side.country')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('trade_name', models.CharField(max_length=250, unique=True)),
                ('international_name', models.CharField(max_length=250, unique=True)),
                ('structure', models.TextField(default='Состав лекарства')),
                ('price', models.FloatField(default=0.0)),
                ('slug', models.SlugField(default='', unique=True)),
                ('_price_increment', models.IntegerField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client_side.manufacturer')),
            ],
            options={
                'ordering': ['-price'],
                'unique_together': {('trade_name', 'international_name')},
            },
        ),
        migrations.CreateModel(
            name='MedicineOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField(default=1)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_side.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('receive_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('delivery_date_time', models.DateTimeField(null=True, verbose_name='Дата выдачи заказа')),
                ('cost', models.FloatField(default=0.0, verbose_name='Стоимость')),
                ('complete', models.BooleanField(default=False, verbose_name='Готовность заказа')),
                ('medicines', models.ManyToManyField(through='client_side.MedicineOrder', to='client_side.medicine', verbose_name='Лекарства')),
            ],
        ),
        migrations.AddField(
            model_name='medicineorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_side.order'),
        ),
    ]
