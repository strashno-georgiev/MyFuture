from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'),
    path('personality_careers/<str:type>', views.personality_carriers, name='carriers'),
    path('personality_careers/career_detail/<str:profession_type>', views.profession_detail, name="career_detail"),
]
