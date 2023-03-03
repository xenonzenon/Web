from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def noysoftwebindex(request):
    template = loader.get_template('noysoftwebindex.html')
    return HttpResponse(template.render())
