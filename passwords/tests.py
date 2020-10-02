from django.urls.base import reverse
from django.test import TestCase
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