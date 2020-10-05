from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('celsius/<str:temperature>/fahrenheit', views.FahrenheitGet, name='celsius'),
    path('fahrenheit/<str:temperature>/celsius', views.CelsiusGet, name='fahrenheit'),
]