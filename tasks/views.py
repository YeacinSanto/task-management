from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management System!")


def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")


def show_task(request):
    return HttpResponse("This is our task page")