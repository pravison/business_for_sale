from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, Paginator
from . models import  CommercialRealEState, Category
from leads.models import Leads
from company.models import User
from company.models import  Information, SocialLink, OurContact
from django.db.models import  Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def commercialRealestate(request):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    realestates = CommercialRealEState.objects.filter(closed_deal=False).order_by('-id')
    paginator = Paginator(realestates, 6)
    page = request.GET.get('page')
    paged_realestates = paginator.get_page(page)
    bizs = CommercialRealEState.objects.order_by('-id')[:5]
    categories = Category.objects.all()

    category_id = request.GET.get('category', 0)
    query = request.GET.get('query')

    if query:
        realestates = realestates.filter(Q(property_description__icontains=query)| Q(title__icontains=query)|Q(locationn__icontains=query)|Q(county__icontains=query)|Q(address__icontains=query))
   
    if category_id :
        realestates = realestates.filter(category__id=category_id )
    context = {
        'infos':infos,
        'links':links,
        'contact_infos': contacts_infos,
        'paged_realestates':paged_realestates,
        'categories': categories,
        'bizs':bizs,
        'realestates': realestates

    }
    return render(request, 'realestate.html', context)

def commercialRealestateView(request, id):
    infos = Information.objects.order_by('id')[:1]
    links = SocialLink.objects.all()
    contacts_infos = OurContact.objects.order_by('id')[:1]
    user = request.user
    realestate = get_object_or_404(CommercialRealEState, id=id)
    relatedRealestates = CommercialRealEState.objects.filter(category = realestate.category).exclude(id = realestate.id)[:5]#reltaed blogs
    
    context = {
        'infos':infos,
        'links':links,
        'contact_infos': contacts_infos,
        'realestate': realestate,
        'user': user,
        'relatedRealestates' : relatedRealestates,
    }
    return render(request, 'realestate-single.html', context)

@login_required
def contactLeads(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        message = request.POST['message']
        user = request.POST['target_user']
        biz = request.POST['business_intrested_in']
        target_user = get_object_or_404(User, id=user) 
        property_intrested_in = get_object_or_404(CommercialRealEState, id=biz) 

        contact = Leads(full_name=full_name, email=email, phone_number=phone_number, message=message, target_user=target_user, property_intrested_in=property_intrested_in )
        contact.save()
        messages.success(request, 'Thanks for reaching out, your message has been submitted succesfully')
        return redirect('/realestate/' + biz + '/')