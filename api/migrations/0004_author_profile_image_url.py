# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_image_url',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
