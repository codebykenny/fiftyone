# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_author_profile_image_url'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('name',)]),
        ),
    ]
