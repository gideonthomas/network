# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-12 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_news_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='excerpt',
            field=models.TextField(blank=True, help_text='A short summary of the article (around 146 characters)', max_length=200, null=True),
        ),
    ]
