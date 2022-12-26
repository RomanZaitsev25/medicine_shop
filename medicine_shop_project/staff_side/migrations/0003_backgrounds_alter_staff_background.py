# Generated by Django 4.1.2 on 2022-12-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_side', '0002_positions_alter_staff_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backgrounds',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('educational_institution', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='background',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff_side.backgrounds'),
        ),
    ]
