from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    return render(request,'mainapp/base.html')
