from django.db import models
from company.models import User
from businesses.models import Businesse
from realestate.models import CommercialRealEState
 

# Create your models here.
class Leads(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    business_intrested_in = models.ForeignKey(Businesse, on_delete=models.DO_NOTHING, blank=True, null=True)
    property_intrested_in = models.ForeignKey(CommercialRealEState, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
