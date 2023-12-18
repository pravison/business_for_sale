from django import forms 
from . models import User
from realestate.models import CommercialRealEState
from businesses.models import Businesse
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RealEStateCreationForm(forms.ModelForm):
    class Meta:
        model = CommercialRealEState
        fields = ( 'title', 'category', 'asking_price', 'property_name', 'owner', 'total_rooms', 'current_occupied_rooms', 'average_montly_rental_income', 'property_description', 'number_of_workers', 'building_photo', 'room_photos_1', 'room_photos_2',
    'room_photos_3', 'room_photos_4','room_photos_5','room_photos_6', 'title_dead_exists', 'property_square_area','property_blue_prints', 'constructed_on','property_disputes',
    'disputes_description', 'repair_needed', 'repair_description', 'country', 'county', 'locationn', 'address')

        widgets ={
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }), 
            'asking_price': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'property_name': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'owner': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'total_rooms': forms.NumberInput(attrs={
                'class': 'form-control'
            }), 
            'current_occupied_rooms': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'average_montly_rental_income': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'property_description': SummernoteWidget(), 
            'number_of_workers': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'building_photo': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'room_photos_1': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'room_photos_2': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'room_photos_3': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'room_photos_4': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'room_photos_5': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'room_photos_6': forms.FileInput(attrs={
                'class': 'form-control'
            }), 
            'title_dead_exists': forms.CheckboxInput(attrs={
            }), 
            'property_square_area': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'property_blue_prints': forms.CheckboxInput(attrs={
            }), 
            'constructed_on': forms.TextInput(attrs={
                'class': 'form-control',
                'type':'date'
            }),
            'property_disputes': forms.CheckboxInput(attrs={
               
            }),
            'disputes_description': SummernoteWidget(), 
            'repair_needed': forms.CheckboxInput(attrs={
                
            }), 
            'repair_description': SummernoteWidget(), 
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'county': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'locationn': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class BusinessCreationForm(forms.ModelForm):
    class Meta:
        model = Businesse
        fields = "__all__"
        exclude = ['listed_by']
        widgets ={
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'industry': forms.Select(attrs={
                'class': 'form-control'
            }), 
            'asking_price': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'business_name': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'business_owner': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'cashflow': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'gross_annual_revenue': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'profits': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'realestate': forms.Select(attrs={
                'class': 'form-control'
            }), 
            'number_of_employes': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'business_photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'inventory': SummernoteWidget(), 
            'description':SummernoteWidget(), 
            'competion': SummernoteWidget(), 
            'support_and_training': SummernoteWidget(), 
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'county': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'lease_expiration': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }