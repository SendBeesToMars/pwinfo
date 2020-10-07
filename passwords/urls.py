from django.urls import path

from . import views

app_name = "passwords"
urlpatterns = [
    path('',        views.index_view,           name='index'),
    path('search',  views.vote,                 name='vote'),
    path('result',  views.result,               name='result'),
    path('config',  views.config_view,           name='config'),
]