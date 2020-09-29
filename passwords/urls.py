from django.urls import path

from . import views

app_name = "passwords"
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/vote/
    path('search', views.vote, name='vote'),
    path('configure', views.configure, name='configure'),
    # ex: /polls/5/vote/
    path('result', views.ResultView.as_view(), name='result'),
    
    path('config', views.ConfigView.as_view(), name='config'),
    # ex: /polls/5/
    # path('<str:pk>/', views.SearchView.as_view(), name='search'),
]