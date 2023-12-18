from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('newsletter', views.NewsLetter, name='newsletter'),
    path('signup/', views.Signup, name='signup'),
    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name ='login'),
    path('logout', views.logout, name='logout'),
    path('add_realestate/', views.addRealestate, name='add_realestate'),
    path('edit_realestate/<int:id>/', views.editRealestate, name='edit_realestate'),
    path('add_business/', views.addBusiness, name='add_business'),
    path('edit_business/<int:id>/', views.editBusiness, name='edit_business'),
]