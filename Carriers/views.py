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
    video_path = "{% static Carriers/" + context['profession'].name + "/video.mp4 %}"
    context['video_path'] = video_path
    return render(request, "Carriers/profession_detail.html", context)


def home(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            context = {
                'professions': Profession.objects.all(),
                'type':type,
            }
            #return render(request, 'Carriers/personality_carriers.html', context);
            return redirect("personality_careers/" + type)
    else:
        form = MyForm();
    context = {
        'form':form,
    }

    return render(request, 'Carriers/home.html', context)



def about(request):
    return render(request, 'Carriers/about.html', {'title': 'About'})
