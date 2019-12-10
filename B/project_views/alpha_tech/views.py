from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'alpha_tech/home.html', {})

def blog(request):
    return render(request, 'alpha_tech/blog.html', {})

def mentor(request):
    return render(request, 'alpha_tech/mentor.html', {})

def mentee(request):
    return render(request, 'alpha_tech/mentee.html', {})

def author(request):
    return render(request, 'alpha_tech/author.html', {})