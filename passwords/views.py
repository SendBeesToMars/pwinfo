from datetime import date
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core import serializers

from .forms import ConfigForm
from django.views.generic.edit import FormView
from .models import Option, Website

# class IndexView(generic.ListView):
#     model = Website
#     template_name = 'passwords/index.html'

def index_view(request):
    return render(request, "passwords/index.html")
    
def config_view(request):
    context = {"name": request.GET.get("search_query", ""), }
    return render(request, "passwords/config.html", context)
        
# def config_view(request):
#     form = ConfigForm(request.POST or None)
#     if form.is_valid:
#         form.save()
    
#     context = {
#         "name": "google.com",
#         "form": form,
#     }
#     return render(request, "passwords/config.html", context)
    
    
def result(request):
    name = request.POST.get("website", "error")
    try:
        # if object already exists in database, display that object, else create new one
        if Website.objects.filter(website_name=name).exists():
            website = get_object_or_404(Website, website_name=name)
            option = get_object_or_404(Option, website_id=website)
        else:
            website = Website(website_name=name, date_added=timezone.now())
            option = Option(website_id=website, 
                            capitals=request.POST.get("capitals", False) == "on",
                            numbers=request.POST.get("numbers", False) == "on",
                            symbols=request.POST.get("symbols", False) == "on",
                            min_len=int(request.POST.get("min_len", 0)),
                            max_len=int(request.POST.get("max_len", 0)),
                            other_details=request.POST.get("other_details", ""),
                            votes=request.POST.get("votes", 0),)
            website.save()
            option.save()
    except:
        return render(request, reverse("passwords:config"), {
            "name": name,
            "error_message": "idk man somethings wrong",
        })
    else:
        # creates key value pair for options model to be displayed 
        options = serializers.serialize( "python", Option.objects.filter(website_id=get_object_or_404(Website, website_name=name)))
        return render(request, "passwords/result.html", {
            "options": options,
            "name":name,
        })

def vote(request):
    name = request.GET.get("search_query", "")
    try:
        options = serializers.serialize( "python", Option.objects.filter(website_id=get_object_or_404(Website, website_name=name)))
    except:
        return render(request, "passwords/index.html", {
            "error_message": "website not found",
            "name": name,
        })
    else:
        return render(request, "passwords/result.html", {
            "options": options,
            "name":name,
        })
    