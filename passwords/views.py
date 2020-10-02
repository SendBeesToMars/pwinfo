from datetime import date
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

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
    
class ConfigView(generic.ListView):
    model = Website
    template_name = 'passwords/config.html'
    context_object_name = 'name'
    
    def get_queryset(self):
        return self.request.GET.get("search_query", "")

class ResultView(generic.ListView):
    model = Website
    template_name = 'passwords/result.html'
    context_object_name = 'testing'
    
    def get_queryset(self):
        return "ResultView"
    
def configure(request):
    name = request.POST["website"]
    try:
        website = Website(website_name=name, date_added=timezone.now())
        option = Option(website_id=website, 
                        capitals=request.POST.get("capitals", False) == "on",
                        numbers=request.POST.get("numbers", False) == "on",
                        symbols=request.POST.get("symbols", False) == "on",
                        min_len=int(request.POST["min_len"]),
                        max_len=int(request.POST["max_len"]),
                        other_details=request.POST["other_details"],
                        votes=request.POST.get("votes", 0),)
    except:
        return render(request, reverse("passwords:config"), {
            'name': name,
            'error_message': "idk man somethings wrong",
        })
    else:
        website.save()
        option.save()
        options = serializers.serialize( "python", Option.objects.filter(website_id=Website.objects.get(website_name=name)))
        return render(request, 'passwords/result.html', {
            'options': options,
            "name":name,
        })

def vote(request):
    name = request.GET.get("search_query", "")
    try:
        options = serializers.serialize( "python", Option.objects.filter(website_id=Website.objects.get(website_name=name)))
    except:
        return render(request, 'passwords/index.html', {
            'error_message': "website not found",
            "name": name,
        })
    else:
        return render(request, 'passwords/result.html', {
            'options': options,
            "name":name,
        })
    