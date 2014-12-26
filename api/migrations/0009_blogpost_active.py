# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20141226_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
