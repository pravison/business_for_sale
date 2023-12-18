from django.urls import path
from . import views
urlpatterns = [
    path('', views.commercialRealestate, name='realestate'),
    path('<int:id>/', views.commercialRealestateView, name='realestate_single'),
    path('contact', views.contactLeads, name='realestate_contact'),
    # path('comment', views.comments,  name='comment'),
    # path('search', views.search,  name='search')
]