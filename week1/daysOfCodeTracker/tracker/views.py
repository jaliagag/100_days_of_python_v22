from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home1(request):
    return HttpResponse('Hola desafiante!')

def demo(self):
    template = loader.get_template('template.html')

    document = template.render()

    return HttpResponse(document)

