# Generated by Django 4.2.1 on 2023-07-03 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_accounts_ordermaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='date_of_purchase',
            field=models.DateField(default=datetime.datetime(2023, 7, 3, 18, 3, 6, 604449)),
        ),
    ]