from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    AGENT = 'agent'
    OWNER = 'owner'
    BUYER = 'buyer'
    USER_CHOICES = [
        (AGENT , "agent"), 
        (OWNER , "owner"),
        (BUYER , "buyer"),
        ]
    full_name  = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=17)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=250, unique=True)
    are_you =models.CharField(choices=USER_CHOICES, max_length=7, blank=True, null=True )

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

class Information(models.Model):
    companyName = models.CharField(max_length=150)
    logo = models.ImageField(blank=True, null=True)
    pitch = models.TextField(max_length=300)
    tagline = models.TextField(max_length=150)

    def __str__(self):
        return self.companyName
    
    @property
    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    

class Newsletter(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.full_name
    
class OurContact(models.Model):
    country = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=17)
    email = models.EmailField()

    def __str__(self):
        return self.address
    
class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    def __str__(self):
        return self.name
