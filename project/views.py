from django.http import HttpResponse
from django.shortcuts import render

# Create your
#
# views here.
from project.models import User


def index (request):
    return HttpResponse("<h1> Project </h1>")
