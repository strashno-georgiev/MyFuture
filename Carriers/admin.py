from django.contrib import admin
from .models import Profession, PersonalityType, ProfessionEvent
# Register your models here.
admin.site.register(Profession)
admin.site.register(PersonalityType)
admin.site.register(ProfessionEvent)