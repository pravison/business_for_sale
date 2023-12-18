from django.contrib import admin
from . models import Newsletter, OurContact, Information, User, SocialLink
# Register your models here.
admin.site.register(Information)
admin.site.register(OurContact)
admin.site.register(Newsletter)
admin.site.register(User)
admin.site.register(SocialLink)
