# Generated by Django 4.1.7 on 2023-08-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=20)),
                ('UserNum', models.IntegerField()),
                ('Amount', models.IntegerField(default='19')),
                ('Time', models.CharField(max_length=20)),
                ('PymentWay', models.CharField(default='19', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
