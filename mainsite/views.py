# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse
from .models import MyBlog
from datetime import datetime
# Create your views here.

def homepage(request):
    template = get_template('homepage.html')
    blogs = MyBlog.objects.all()
    print blogs
    time_now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def blog_detail(request, mSlug):
    template = get_template('blog_detail.html')
    try:
        blog = MyBlog.objects.get(slug=mSlug)
        if blog != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def test(request):
    template = get_template('test.html')
    html = template.render(locals())
    return HttpResponse(html)