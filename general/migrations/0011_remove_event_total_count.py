# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-04 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_event_total_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='total_count',
        ),
    ]
