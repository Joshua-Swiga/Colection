from django.db import models
from django.contrib.auth.models import User
from Marvels_Website.__init__ import *

# Create your models here.
class Home_Page(models.Model):
    home_title=models.CharField(max_length=300)
    home_introduction=models.TextField()

    def __str__(self) -> str:
        return f"{self.home_title}: {self.home_introduction}"
    


class About_Page(models.Model):
    about_title=models.CharField(max_length=300)
    about_introduction=models.TextField()
    
    def __str__(self) -> str:
        return f"{self.about_title}: {self.about_introduction}"



class Services_Page(models.Model):
    #service_icon=models.ImageField(upload_to='app_website/images/service_icons')
    service_title=models.CharField(max_length=300)
    service_description=models.TextField()

    def __str__(self) -> str:
        return f"{self.service_title}: {self.service_description}"



class Events_Page(models.Model):
    event_date=models.DateField(auto_now=True)
    event_name=models.CharField(max_length=100, default =False)
    thumbnail_image=models.ImageField(upload_to='images/event_thumbnails', default=False)
    full_event_images=models.ImageField(upload_to='images/event_images', default=False)
    description=models.TextField(default =Description)
    logistics=models.TextField(default =Logistics)
    prerequisites=models.TextField(default =Prerequisites)
    payment_details=models.TextField(default =Details)
    
    def __str__(self) -> str:
        return f'{self.event_name}'
    


class Inquiries_and_Messages(models.Model):
    sender_name=models.CharField(max_length=1000)
    sender_email=models.EmailField()
    sender_phone_number=models.PositiveIntegerField()
    sener_message=models.TextField()

    def __str__(self) -> str:
        return f"{self.sender_name}"
    

class Blog_Posts(models.Model):
    date_written=models.DateField(auto_now=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100, blank=True, null=True)
    body=models.TextField()

    def __str__(self) -> str:
        return f'{self.title}: By {self.author}'