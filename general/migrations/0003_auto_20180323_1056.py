# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-23 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20180323_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='payment',
            field=models.CharField(choices=[('CASH', 'cash'), ('PAYTM', 'paytm')], max_length=5),
        ),
    ]
