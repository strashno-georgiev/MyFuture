from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profession, PersonalityType, ProfessionEvent

from .forms import CodeForm
from django.contrib import messages

def personality_carriers(request, type):
    valid_professions = Profession.objects.filter(tags__contains=type)
    try:
        personality_type = PersonalityType.objects.filter(code=str(type))[0]
    except:
        raise Http404("Personality type does not exist.")
    events = ProfessionEvent.objects.all()
    valid_events = []
    for event in events:
        if event.profession in valid_professions:
            valid_events.append(event)
    context = {
        'professions':valid_professions,
        'personality':personality_type,
        'events': valid_events,
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
        form = CodeForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            context = {
                'professions': Profession.objects.all(),
                'type':type,
            }
            #return render(request, 'Carriers/personality_carriers.html', context);
            return redirect("personality_careers/" + type)
    else:
        form = CodeForm();
    context = {
        'form':form,
    }

    return render(request, 'Carriers/home.html', context)



def about(request):
    return render(request, 'Carriers/about.html', {'title': 'About'})

def events_page(request):
    context = {
        'events': ProfessionEvent.objects.all()
    }
    return render(request, 'Carriers/events.html', context)