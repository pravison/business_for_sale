from django.urls import path
from . import views
urlpatterns = [
    path('', views.businesses, name='biz'),
    path('<int:id>/', views.businessView, name='biz_single'),
    path('contact', views.contactMessage, name='contact'),
    # path('comment', views.comments,  name='comment'),
    # path('search', views.search,  name='search')
]