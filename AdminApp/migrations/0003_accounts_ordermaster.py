# Generated by Django 4.2.1 on 2023-07-03 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
        ('AdminApp', '0002_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=20000)),
            ],
            options={
                'db_table': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField(default=datetime.datetime(2023, 7, 3, 18, 0, 8, 124061))),
                ('amount', models.FloatField(default=2000)),
                ('details', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'OrderMaster',
            },
        ),
    ]
