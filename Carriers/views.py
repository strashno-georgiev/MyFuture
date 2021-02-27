from django.shortcuts import render
from django.http import HttpResponse
from .models import Profession
def estj(request):
    context = {
        'professions':Profession.objects.all(),
    }
    return render(request, "Carriers/estj.html", context)


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {

        'posts': posts
    }

    return render(request, 'Carriers/home.html', context)



def about(request):
    return render(request, 'Carriers/about.html', {'title': 'About'})
