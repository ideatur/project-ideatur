# Generated by Django 3.1.1 on 2020-09-23 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='date',
        ),
    ]
