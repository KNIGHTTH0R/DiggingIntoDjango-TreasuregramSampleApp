# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_treasure_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasure',
            name='img_url',
        ),
        migrations.AddField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='default.png', upload_to=main_app.models.get_image_path),
            preserve_default=False,
        ),
    ]
