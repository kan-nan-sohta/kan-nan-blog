from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': 'This is sample page',
        'goto': 'next',
    }
    # return HttpResponse('Hello from Python!')
    return render(request, "hello/index.html", params)

def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': 'This is another page',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
