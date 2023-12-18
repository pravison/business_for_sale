from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, Paginator
from django.contrib.auth.decorators import login_required
from . models import  Categories, Businesse, Industry
from leads.models import Leads
from company.models import User
from company.models import  Information, SocialLink, OurContact
from django.db.models import  Q
from django.contrib import messages

# Create your views here.

def businesses(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    businesses = Businesse.objects.filter(closed_deal=False).order_by('-id')
    paginator = Paginator(businesses, 6)
    page = request.GET.get('page')
    paged_businesses = paginator.get_page(page)
    bizs = Businesse.objects.order_by('-id')[:5]
    categories = Categories.objects.all()
    industries = Industry.objects.all()
    category_id = request.GET.get('category', 0)
    industry_id = request.GET.get('industry', 0)
    query = request.GET.get('query')

    if query:
        businesses = businesses.filter(Q(description__icontains=query)| Q(title__icontains=query)|Q(location__icontains=query)|Q(county__icontains=query)|Q(address__icontains=query))
   
    if category_id :
        businesses = businesses.filter(category__id=category_id )
    if industry_id :
        businesses = businesses.filter(industry__id=industry_id )
    context = {
        'infos':infos,
        'links':links,
        'contact_infos': contacts_infos,
        'paged_businesses':paged_businesses,
        'categories': categories,
        'industries': industries,
        'bizs':bizs,
        'businesses': businesses

    }
    return render(request, 'businesses.html', context)
@login_required
def businessView(request, id):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    biz = get_object_or_404(Businesse, id=id)
    user = request.user
    relatedBiz = Businesse.objects.filter(category = biz.category).exclude(id = biz.id)[:5]#reltaed blogs
    
    context = {
        'infos':infos,
        'links':links,
        'contact_infos': contacts_infos,
        'biz': biz,
        'user': user,
        'relatedBiz' : relatedBiz,
    }
    return render(request, 'business-single.html', context)

def contactMessage(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        message = request.POST['message']
        user = request.POST['target_user']
        biz = request.POST['business_intrested_in']
        target_user = get_object_or_404(User, id=user) 
        business_intrested_in = get_object_or_404(Businesse, id=biz) 

        contact = Leads(full_name=full_name, email=email, phone_number=phone_number, message=message, target_user=target_user, business_intrested_in=business_intrested_in )
        contact.save()
        messages.success(request, 'Thanks for reaching out, your message has been submitted succesfully')
        return redirect('/businesses/' + biz + '/')
    
