# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20141226_1524'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([]),
        ),
    ]
