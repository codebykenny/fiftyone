# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20141226_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
