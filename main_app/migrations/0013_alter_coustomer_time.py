# Generated by Django 4.1.7 on 2023-08-18 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_coustomer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 19, 23, 18, 410779), max_length=20, null=True, verbose_name='التاريخ و الوقت'),
        ),
    ]
