# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-24 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20180323_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
    ]
