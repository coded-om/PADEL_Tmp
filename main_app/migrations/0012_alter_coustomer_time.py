# Generated by Django 4.1.7 on 2023-08-18 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_coustomer_pymentway_alter_coustomer_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 19, 22, 40, 607293), max_length=20, null=True, unique=True, verbose_name='التاريخ و الوقت'),
        ),
    ]
