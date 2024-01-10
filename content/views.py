from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    content = Content.objects.all().last()
    banner = BannerContent.objects.all().last()
    faq = Faq.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    services = Services.objects.all()
    navlist = Navigation.objects.all()
    context={
        'content':content,
        'banner':banner,
        'faq':faq,
        'aboutus':aboutus,
        'socialmedia':socialmedia,
        'services':services,
    'navlist':navlist,
    }
    return render(request,"home.html",context)

def index(request):
    content = Content.objects.all().last()
    banner = BannerContent.objects.all().last()
    faq = Faq.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    services = Services.objects.all()
    navlist = Navigation.objects.all().order_by("-id")
    context={
        'services':services,
        'content':content,
        'banner':banner,
        'faq':faq,
        'aboutus':aboutus,
        'socialmedia':socialmedia,
        'navlist':navlist,
    }
    return render(request,"index.html",context)

def contact_detail(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        name         = request.POST.get('name')
        email        = request.POST.get('email')
        message         = request.POST.get('message')
        phone       = request.POST.get('phone')
        data         = Contact_Us(name=name,email=email,phone=phone,message=message)
        data.save()
        messages.success(request,"we,ve get your contact will reached you soon")
        return redirect(url)

def subscribe(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        email = request.POST.get('email')
        data = Subscription(email=email)
        data.save()
        messages.success(request,"Thankyou to subscribe our newsletter")
    return redirect(url)

def contact_view(request):
    services = Services.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    navlist = Navigation.objects.all()
    context={
        'aboutus':aboutus,
        "socialmedia":socialmedia,
        'services':services,
        'navlist':navlist,
    }
    return render(request,'contact.html',context)

def contact_view_ar(request):
    services = Services.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    navlist = Navigation.objects.all().order_by("-id")
    context={
        'aboutus':aboutus,
        "socialmedia":socialmedia,
        'services':services,
        'navlist':navlist,
    }
    return render(request,'contact_ar.html',context)

def Image_gallery(request):
    services = Services.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    img = ImageGallery.objects.all()
    navlist = Navigation.objects.all()
    context={
        'aboutus':aboutus,
        "socialmedia":socialmedia,
        'services':services,
        'img':img,
        'navlist':navlist,
    }
    return render(request,'ImageGallery.html',context)

def Image_gallery_ar(request):
    services = Services.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    img = ImageGallery.objects.all()
    navlist = Navigation.objects.all().order_by("-id")
    context={
        'aboutus':aboutus,
        "socialmedia":socialmedia,
        'services':services,
        'img':img,
        'navlist':navlist,
    }
    return render(request,'ImageGallery_ar.html',context)