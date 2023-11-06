from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place
from . models import person
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request, "index.html",{'result':obj,'res':obj1})



#def addition(request):
    #x = int(request.GET['number1'])
    #y = int(request.GET['num2'])
    #res = x + y
    #return render(request, "result.html", {'result': res})


