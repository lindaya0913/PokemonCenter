# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def app_homepage(request):
    return  render(request, 'homepage.html')
def about_us(request):
    return  render(request, 'aboutus.html')
def services(request):
    return  render(request, 'services.html')
def contact_us(request):
    return  render(request, 'contactus.html')
