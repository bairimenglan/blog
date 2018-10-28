# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mainsite.models import MyBlog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_date')

admin.site.register(MyBlog, BlogAdmin)


