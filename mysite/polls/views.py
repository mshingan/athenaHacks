from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
    #return HttpResponse("Hello, world. You're at the polls index.")
