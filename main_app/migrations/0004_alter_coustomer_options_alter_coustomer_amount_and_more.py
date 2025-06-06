# Generated by Django 4.1.7 on 2023-08-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_coustomer_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coustomer',
            options={'verbose_name': 'Consumer'},
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='Amount',
            field=models.IntegerField(default='19', verbose_name='السعر'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='PymentWay',
            field=models.CharField(default='19', max_length=20, verbose_name='طريقه الدفع'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='Time',
            field=models.CharField(max_length=20, verbose_name='التوقيت'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='UserName',
            field=models.CharField(default='اسم العميل', max_length=20, verbose_name='اسم العميل'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='UserNum',
            field=models.IntegerField(max_length=8, verbose_name='رقم الهاتف'),
        ),
    ]
