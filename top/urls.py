from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'top'),
    path('about/', views.about, name = 'about'),
]
