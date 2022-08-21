from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('playgroud/hello', views.say_hello)
]