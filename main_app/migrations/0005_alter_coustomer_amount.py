# Generated by Django 4.1.7 on 2023-08-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_coustomer_options_alter_coustomer_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='Amount',
            field=models.IntegerField(default='00', max_length=2, verbose_name='السعر'),
        ),
    ]
