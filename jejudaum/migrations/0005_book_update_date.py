# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jejudaum', '0004_remove_book_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='update_date',
            field=models.DateTimeField(null=True),
        ),
    ]
