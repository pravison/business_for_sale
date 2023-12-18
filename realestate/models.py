from django.db import models
from company.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class CommercialRealEState(models.Model):
    title = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    asking_price = models.CharField(max_length=150)
    property_name = models.CharField(max_length=200)
    owner = models.TextField(max_length=300)
    total_rooms = models.CharField(max_length=100)
    current_occupied_rooms = models.CharField(max_length=100)
    average_montly_rental_income = models.CharField(max_length=100)
    property_description = models.TextField(blank=True, null=True)
    number_of_workers = models.IntegerField(default=0)
    building_photo = models.ImageField(blank=True, null=True)
    room_photos_1 = models.ImageField(blank=True, null=True)
    room_photos_2 = models.ImageField(blank=True, null=True)
    room_photos_3 = models.ImageField(blank=True, null=True)
    room_photos_4 = models.ImageField(blank=True, null=True)
    room_photos_5 = models.ImageField(blank=True, null=True)
    room_photos_6 = models.ImageField(blank=True, null=True)

    title_dead_exists = models.BooleanField(default=False) 
    property_square_area = models.CharField(max_length=100, blank=True, null=True)
    property_blue_prints = models.BooleanField(default=False)
    constructed_on = models.DateField(blank=True, null=True)

    property_disputes= models.BooleanField(default=False)
    disputes_description = models.TextField(blank=True, null=True)
    repair_needed = models.BooleanField(default=False)
    repair_description = models.TextField(blank=True, null=True)

    country = models.CharField(max_length=150)
    county =models.CharField(max_length=150)
    locationn = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    featured = models.BooleanField(default=False)
    closed_deal = models.BooleanField(default=False) 

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.building_photo.url
            
        except:
            url = ''

        return url 
    @property
    def photoURL(self):
        try:
            url = self.room_photos_1.url
            
        except:
            url = ''

        return url 
    
    @property
    def photo1URL(self):
        try:
            url = self.room_photos_2.url
            
        except:
            url = ''

        return url 
    
    @property
    def photo2URL(self):
        try:
            url = self.room_photos_3.url
            
        except:
            url = ''

        return url 
    @property
    def photo3URL(self):
        try:
            url = self.room_photos_4.url
            
        except:
            url = ''

        return url 
    @property
    def photo4URL(self):
        try:
            url = self.room_photos_5.url
            
        except:
            url = ''

        return url 
    @property
    def photo5URL(self):
        try:
            url = self.room_photos_6.url
            
        except:
            url = ''

        return url 
    


