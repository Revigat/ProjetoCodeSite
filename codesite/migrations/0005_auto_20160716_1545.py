# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesite', '0004_pessoa_mensagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='mensagem',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
