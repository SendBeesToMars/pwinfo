from django.urls import path

from . import views

app_name = "passwords"
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<str:pk>/', views.SearchView.as_view(), name='search'),
    # ex: /polls/5/vote/
    path('search', views.vote, name='vote'),
    # ex: /polls/5/vote/
    path('result', views.ResultView.as_view(), name='result'),
]