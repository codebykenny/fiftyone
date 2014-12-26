# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('blurb', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=5000)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('modified', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, to='api.Author', null=True)),
                ('blog', models.ForeignKey(to='api.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
