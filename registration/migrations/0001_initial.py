# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=255, verbose_name='Surname')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('school', models.CharField(max_length=255, verbose_name='School')),
                ('grade_level', models.CharField(max_length=255, verbose_name='Grade level')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('province', models.CharField(max_length=255, verbose_name='Province')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email address')),
                ('preferred_course_start', models.CharField(max_length=3, verbose_name='Preferred course start', choices=[(b'Mar', 'March'), (b'Apr', 'April'), (b'May', 'May')])),
            ],
        ),
    ]
