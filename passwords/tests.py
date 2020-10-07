from django.urls.base import reverse
from django.test import TestCase, Client
from django.utils import timezone
from .models import Website
from django.urls import reverse


class WebsiteModelTests(TestCase):
    def create_website(self, website_name="test name :)", date_added=timezone.now()):
        return Website(website_name=website_name, date_added=date_added)

    def test_website_creation(self):
        w = self.create_website()
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
    
    
    
# from django.test import Client
# c = Client()
# response = c.post("/login/", {"username": "john", "password": "smith"})
# response.status_code
# response = c.get("/customer/details/")
# response.content