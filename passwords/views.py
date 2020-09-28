from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers

from .models import Option, Website


class IndexView(generic.ListView):
    model = Website
    template_name = 'passwords/index.html'
    
    def get_queryset(self):
        return "IndexView"
    

class SearchView(generic.ListView):
    model = Website
    template_name = 'passwords/search.html'
    context_object_name = 'testing'
    
    def get_queryset(self):
        # return "what arm thing homie?"
        return "SearchView"

class ResultView(generic.ListView):
    model = Website
    template_name = 'passwords/result.html'
    context_object_name = 'testing'
    
    def get_queryset(self):
        # return "what arm thing homie?"
        return "ResultView"

def vote(request):
    name = request.GET.get("search_query", "")
    try:
        # options = get_object_or_404(Option ,website=Website.objects.get(website_name=name))
        # gets key value pair for options model using the get requests website name
        options = serializers.serialize( "python", Option.objects.filter(website_id=Website.objects.get(website_name=name)))
    except:
        return render(request, 'passwords/index.html', {
            'error_message': "website not found",
        })
    else:
        # return HttpResponseRedirect(reverse('passwords:result'))
        return render(request, 'passwords/result.html', {
            'options': options,
            "name":name,
        })
    