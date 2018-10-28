# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class MyBlog(models.Model):

    blogtag = (
        ('linux','ubuntu linux'),
        ('ucos', 'rtos rutine'),
        ('mpu', '处理器'),
        ('mcu', '单片机'),
        ('qt', 'qt 相关的东西'),
    )

    title = models.CharField(u'文章标题', max_length=200)
    slug = models.CharField(u'文章编号', max_length=200)
    body = models.TextField(u'文章内容')
    pub_date = models.DateField(u'发布日期')
    pub_time = models.TimeField(u'发布时间')
    tags = models.CharField(u'标签',max_length=20,choices=blogtag,default='linux')

    def __unicode__(self):
        return self.title
