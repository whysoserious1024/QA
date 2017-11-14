# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-08 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20171108_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionType',
            field=models.CharField(choices=[('0', '电脑问题'), ('1', 'OA系统问题'), ('2', 'NC系统问题'), ('3', '账号密码重置')], default='0', max_length=1, verbose_name='问题分类'),
        ),
    ]