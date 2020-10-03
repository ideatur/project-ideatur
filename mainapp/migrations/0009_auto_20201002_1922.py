# Generated by Django 3.1.1 on 2020-10-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20201002_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtour',
            name='airport_from',
            field=models.CharField(choices=[('бориспіль', 'Київ-Бориспіль'), ('жуляни', 'Київ-Жуляни')], max_length=100, verbose_name='Виліт з'),
        ),
        migrations.AlterField(
            model_name='newtour',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Місто'),
        ),
        migrations.AlterField(
            model_name='newtour',
            name='hotel',
            field=models.CharField(max_length=100, verbose_name='Готель'),
        ),
    ]
