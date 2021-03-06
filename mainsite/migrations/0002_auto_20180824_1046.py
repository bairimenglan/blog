# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myblog',
            old_name='pub_dat',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='myblog',
            name='body',
            field=models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='\u6587\u7ae0\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u6587\u7ae0\u6807\u9898'),
        ),
    ]
