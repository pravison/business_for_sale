from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . models import Information, SocialLink, OurContact, Newsletter, User
from django.contrib.auth import authenticate, login, logout
from .forms import RealEStateCreationForm, BusinessCreationForm
from businesses.models import Businesse
from realestate.models import CommercialRealEState
from blog.models import Blog
from leads.models import Leads


# Create your views here
def homepage(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    businesses = Businesse.objects.filter(featured=True)[:6]
    realestates =CommercialRealEState.objects.filter(featured=True)[:6]
    blogs = Blog.objects.all().order_by('id')[:3]
    # paginator = Paginator(blogs, 5)
    # page = request.GET.get('page')
    # paged_blogs = paginator.get_page(page)
    # posts = Blog.objects.order_by('-dateUpdated')[:5]
    # tags = Tag.objects.all()
    # categories = Categories.objects.all()
    context = {
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
        'businesses': businesses,
        'realestates': realestates,
        'blogs': blogs
    }
    return render(request, 'homepage.html', context)

def NewsLetter(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']

        newsletter = Newsletter(email=email, full_name=full_name)
        newsletter.save()
        messages.success(request, 'thanks for subscribing to our newsletter!')
        return redirect('homepage')

def Signup(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        full_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        are_you = request.POST['are_you']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(
                full_name = full_name,
                username= username,
                email= email,
                password=password1,
                phone=phone,
                are_you=are_you
            )
            login(request, user)
            messages.success(request, 'Thanks for joining our team ')
            return redirect('/')
        else:
          context={
            'infos' : infos,
            'links' : links,
            'contacts_infos':contacts_infos,
          }
          messages.success(request, 'password does not match')
          return render(request, 'signup.html', context)  

        
    else:
        return render(request, 'signup.html')
    
def login(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            messages.success(request, 'Thanks for joining our team ')
            return redirect('/')         
    else:
        context = {
            'infos':infos,
            'links':links,
            'contact_infos': contacts_infos,
        }
        return render(request, 'login.html', context)
    
def logout(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    user = request.user
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    businesses = Businesse.objects.filter(listed_by=user)
    realestates =CommercialRealEState.objects.filter(listed_by=user)
    blogs = Blog.objects.all().order_by('id')[:3]
    leads =  Leads.objects.filter(target_user=user)
    context= {
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
        'businesses': businesses,
        'realestates': realestates,
        'blogs': blogs,
        'leads': leads
    }
    return render(request, 'dashboard.html', context)

def addRealestate(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    user = request.user
    if request.method == 'POST':
        form = RealEStateCreationForm(request.POST , request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.listed_by = user
            listing.save()

            return redirect('dashboard')
    else:
        form = RealEStateCreationForm()
    context = {
        'form': form,
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
    }
    return render(request, 'add_realestate.html', context)

def editRealestate(request, id):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    if request.method == 'POST':
        realestate= CommercialRealEState.objects.get(id=id)
        form = RealEStateCreationForm(request.POST, instance=realestate)
        biz = str(realestate.id)
        if form.is_valid():
            form.save()
            context= {
                'form': form,
                'realestate': realestate,
                'success': True
                }
            messages.success(request, 'Listing Edited Succesfully ')
            return redirect('/realestate/' + biz + '/')
    else:
        realestate= CommercialRealEState.objects.get(id=id)
        form = RealEStateCreationForm(instance=realestate)

    context= {
                'form': form,
                'realestate': realestate,
                'infos':infos,
                'links':links,
                'contact_infos': contacts_infos,
            }
    return render(request, 'edit_realestate.html', context)
    
#@login_required
def delete(request, id):
    listing = get_object_or_404(CommercialRealEState, id=id)
    listing.delete()
    return redirect('dashboard')


def addBusiness(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    user = request.user
    if request.method == 'POST':
        form = BusinessCreationForm(request.POST , request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.listed_by = user
            listing.save()

            return redirect('dashboard')
    else:
        form = BusinessCreationForm()
    context = {
        'form': form,
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
    }
    return render(request, 'add_business.html', context)

def editBusiness(request, id):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    if request.method == 'POST':
        business= Businesse.objects.get(id=id)
        biz = str(business.id)
        form = BusinessCreationForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            context= {
                'form': form,
                'business': business,
                'success': True
                }
            messages.success(request, 'Listing Edited Succesfully ')
            return redirect('/businesses/' + biz + '/')
    else:
        business= Businesse.objects.get(id=id)
        form = BusinessCreationForm(instance=business)

    context= {
                'infos':infos,
                'links':links,
                'contact_infos': contacts_infos,
                'form': form,
                'business': business
            }
    return render(request, 'edit_business.html', context)
    
#@login_required
def deleteBusiness(request, id):
    listing = get_object_or_404(Businesse, id=id)
    listing.delete()
    return redirect('dashboard')
