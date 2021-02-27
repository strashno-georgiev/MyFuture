from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profession

from .forms import MyForm
from django.contrib import messages

def estj(request):
    if(request.type == GET):
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

    form = MyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            type = form.cleaned_data.get('type')
            print("\n\n\n\n\n\n\n", type ,"\n\n\n\n\n\n\n")
            messages.success(request, f'Jobs fot  {type}!')
            return redirect('pages-home')

    context = {

        'posts': posts,
        'form':form,
    }

    return render(request, 'Carriers/home.html', context)



def about(request):
    return render(request, 'Carriers/about.html', {'title': 'About'})
