from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

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
    # website = get_object_or_404(Website, pk=website_name)
    name = request.GET.get("search_query", "")
    selected_website = get_object_or_404(Website, website_name=name)
    try:
        # options = selected_website.option_set.get(website="2")
        options = get_object_or_404(Option ,website=selected_website.id)
    except (KeyError, Option.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'passwords/search.html', {
            'website': selected_website,
            'error_message': "Some error has occured :/",
        })
    else:
        # selected_website.votes += 1
        # selected_website.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('passwords:result'))
        return render(request, 'passwords/result.html', {
            'options': options,
        })
    