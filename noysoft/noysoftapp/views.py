from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def noysoftappindex(request):
    template = loader.get_template('noysoftappindex.html')
    return HttpResponse(template.render())
