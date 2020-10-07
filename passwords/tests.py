from django.urls.base import reverse
from django.test import TestCase, Client
from django.utils import timezone
from .models import Website, Option
from django.urls import reverse
from django.shortcuts import get_object_or_404

def create_website(website_name="test name :)", date_added=timezone.now()):
    return Website(website_name=website_name, date_added=date_added)

def create_option(website_id, capitals=False, numbers=True,
                   symbols=True, min_len=233, max_len=97643, 
                   other_details="other deets"):
    return Option(website_id=website_id, capitals=capitals,
                    numbers=numbers, symbols=symbols, min_len=min_len,
                    max_len=max_len, other_details=other_details)

class WebsiteModelTests(TestCase):

    def test_website_creation(self):
        w = create_website()
        self.assertTrue(isinstance(w, Website))
        self.assertEqual(w.__str__(), w.website_name)
        
class IndexViewTests(TestCase):
    def test_website_list_view(self):
        url = reverse("passwords:index")
        resp = self.client.get(url)
        
        self.assertContains(resp, "Enter Website Name :)", status_code=200)
        
class ConfigViewTests(TestCase):
    def test_get_request(self):
        url = "/passwords/config?search_query=test122"
        resp = self.client.get(url)
        
        self.assertContains(resp, "test122", status_code=200)
        
class ResultViewTests(TestCase):
    def test_form_post_request(self):
        c = Client()
        resp = c.post("/passwords/result", {"website": "test_website",
                                            "numbers": "on","password": "on", 
                                            "min_len": 987216319, "max_len": 12, 
                                            "other_details": "hello this is a test :)"})
                
        self.assertContains(resp, "hello this is a test :)", status_code=200)
        self.assertContains(resp, "www.test_website")
        self.assertContains(resp, "987216319")
        self.assertContains(resp, """<th>capitals</th>
                        <td> False</td>""")
    
class VoteViewTests(TestCase):
    def test_vote(self):
        website = create_website("test_website")
        options = create_option(website_id=website)
        website.save()
        options.save()
        
        url = "/passwords/search?search_query=test_website"
        resp = self.client.get(url)
        
        self.assertContains(resp, "other deets", status_code=200)
        
    def test_webpage_not_found(self):
        url = "/passwords/search?search_query=test_website"
        resp = self.client.get(url)
        
        self.assertContains(resp, "website not found", status_code=200)
        