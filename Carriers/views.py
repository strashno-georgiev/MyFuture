from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profession

from .forms import MyForm
from django.contrib import messages

def personality_carriers(request, type):
    context = {
        'professions': Profession.objects.all(),
        'type': type,
    }
    return render(request, "Carriers/personality_carriers.html", context)

def profession_detail(request, profession_type):
    context = {
        'profession': Profession.objects.filter(name=profession_type)[0],
    }

    return render(request, "Carriers/profession_detail.html", context)


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

    form = MyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            type = form.cleaned_data.get('type')
            context = {
                'professions': Profession.objects.all(),
                'type':type,
            }
            #return render(request, 'Carriers/personality_carriers.html', context);
            return redirect("personality_careers/" + type)
    context = {

        'posts': posts,
        'form':form,
    }

    return render(request, 'Carriers/home.html', context)



def about(request):
    return render(request, 'Carriers/about.html', {'title': 'About'})
