from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('privacy-policy/',views.privacypolicy,name="privacypolicy"),
    path('services/',views.services,name="services"),
]