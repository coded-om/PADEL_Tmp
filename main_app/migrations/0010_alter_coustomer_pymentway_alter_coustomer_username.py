# Generated by Django 4.1.7 on 2023-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_coustomer_date_alter_coustomer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='PymentWay',
            field=models.CharField(default='visa', max_length=20, verbose_name='طريقه الدفع'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='UserName',
            field=models.CharField(help_text='اكتب اسم العميل', max_length=20, verbose_name='اسم العميل'),
        ),
    ]
