from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def noysoftgameindex(request):
    template = loader.get_template('noysoftgameindex.html')
    return HttpResponse(template.render())
