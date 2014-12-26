# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(blank=True, to='api.Author', null=True),
            preserve_default=True,
        ),
    ]
