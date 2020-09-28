from django.db import models


# Create your models here.
class Website(models.Model):
    website_name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date added")
    def __str__(self):
        return self.website_name
    
class Option(models.Model):
    website_id = models.ForeignKey(Website, on_delete=models.CASCADE)
    capitals = models.BooleanField(default=False)
    numbers = models.BooleanField(default=False)
    symbols = models.BooleanField(default=False)
    min_length = models.IntegerField(default=0)
    max_length = models.IntegerField(default=0)
    other_details = models.CharField(max_length=500, blank=True)
    votes = models.IntegerField(default=0)