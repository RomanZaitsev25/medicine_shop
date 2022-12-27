# Generated by Django 4.1.4 on 2022-12-27 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_side', '0003_backgrounds_alter_staff_background'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backgrounds',
            options={'verbose_name': 'Уч. заведение', 'verbose_name_plural': 'Уч. заведения'},
        ),
        migrations.AlterModelOptions(
            name='positions',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['second_name'], 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AddField(
            model_name='backgrounds',
            name='full_education',
            field=models.CharField(choices=[('FULL', 'Полное'), ('NOT_FULL', 'Неполное')], default='FULL', max_length=50, verbose_name='Полное образование'),
        ),
        migrations.AlterField(
            model_name='backgrounds',
            name='educational_institution',
            field=models.CharField(max_length=250, verbose_name='Учебное заведение'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='post_name',
            field=models.CharField(max_length=250, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='positions',
            name='responsibility',
            field=models.CharField(max_length=1000, verbose_name='Обязанности'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='_salary',
            field=models.FloatField(default=0.0, verbose_name='ЗП, $'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='background',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff_side.backgrounds', verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff_side.positions', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='schedule_type',
            field=models.CharField(choices=[('FLEXIBLE', 'Flexible'), ('FULL_TIME', 'Full time')], default='FULL_TIME', max_length=250, verbose_name='Расписание'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='second_name',
            field=models.CharField(max_length=250, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='vacations',
            field=models.IntegerField(default=25, verbose_name='Дней отпуска'),
        ),
    ]