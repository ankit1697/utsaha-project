# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-24 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20180324_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
