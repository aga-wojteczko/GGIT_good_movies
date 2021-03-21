from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie

# Create your views here.
import datetime
def hello_world(request):
    return render(request, template_name="base.html")

def my_profile(request):
    my_context = {"time": datetime.datetime.now()}
    return render(request, template_name="my_profile.html",context=my_context)

def movies(request):
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="movies.html",context=my_context)

def index(request):
    return render(request, template_name="index.html")

def subpage(request):
    return render(request, template_name="subpage.html")

def login(request):
    return render(request, template_name="registration/login.html")

from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        form = UserCreationForm()
    return render(request, template_name="registration/signup_form.html",
    context={'form':form})
