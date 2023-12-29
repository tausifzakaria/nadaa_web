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
    context={
        'content':content,
        'banner':banner,
        'faq':faq,
        'aboutus':aboutus,
        'socialmedia':socialmedia,
    }
    return render(request,"home.html",context)

def index(request):
    content = Content.objects.all().last()
    banner = BannerContent.objects.all().last()
    faq = Faq.objects.all()
    aboutus = AboutUs.objects.all().last()
    socialmedia = SocialMedia.objects.all()
    context={
        'content':content,
        'banner':banner,
        'faq':faq,
        'aboutus':aboutus,
        'socialmedia':socialmedia,
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
