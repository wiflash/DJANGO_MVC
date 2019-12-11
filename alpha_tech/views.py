from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request, 'alpha_tech/home.html', {})

def blog(request):
    fields = {"posts": Blog.objects.all()[::-1]}
    return render(request, 'alpha_tech/blog.html', fields)

def mentor(request):
    fields = {"mentors": Mentor.objects.all()}
    return render(request, 'alpha_tech/mentor.html', fields)

def mentee(request):
    fields = {"mentees": Mentee.objects.all()}
    return render(request, 'alpha_tech/mentee.html', fields)

def author(request):
    return render(request, 'alpha_tech/author.html', {})

def post(request, blog_id):
    fields = {"post": Blog.objects.get(pk=blog_id)}
    return render(request, 'alpha_tech/blog-post.html', fields)

def form(request):
    return render(request, 'alpha_tech/blog-form.html', {})

def submit(request):
    post = Blog(
        picture = request.POST['picture'],
        title = request.POST['title'],
        content = request.POST['content']
    )
    post.save()
    return redirect('blog/')