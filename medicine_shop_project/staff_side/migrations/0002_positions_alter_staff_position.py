# Generated by Django 4.1.2 on 2022-12-22 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_side', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('post_name', models.CharField(max_length=250)),
                ('responsibility', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff_side.positions'),
        ),
    ]
