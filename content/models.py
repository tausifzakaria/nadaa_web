from django.db import models

# Create your models here.
class BannerContent(models.Model):
    banner_header_english = models.CharField(max_length=625)
    banner_contnet_english = models.TextField()
    banner_header_arabic = models.CharField(max_length=625)
    banner_contnet_arabic = models.TextField()
    def __str__(self):
        return str(self.banner_header_english)

class Content(models.Model):
    story_header_english = models.CharField(max_length=625)
    story_contnet_english = models.TextField()
    story_header_arabic = models.CharField(max_length=625)
    story_contnet_arabic = models.TextField()
    def __str__(self):
        return str(self.story_header_english)

# class Pricing(models.Model):
#     started_price = models.IntegerField(default=0)
#     professional_price = models.IntegerField(default=0)
#     expert_price = models.IntegerField(default=0)
#     ultimate_price = models.IntegerField(null=True,blank=True,default=0)

class Faq(models.Model):
    title = models.CharField(max_length=255)
    answer = models.TextField()
    title_arabic = models.CharField(max_length=255)
    answer_arabic = models.TextField()
    def __str__(self):
        return str(self.title)

class AboutUs(models.Model):
    text = models.TextField()
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=13)
    email = models.EmailField()
    text_arabic = models.TextField()
    location_arabic = models.CharField(max_length=100)
    contact_no_arabic = models.CharField(max_length=13)
    email_arabic = models.EmailField()
    def __str__(self):
        return str(self.contact_no)

class SocialMedia(models.Model):
    instagram_link = models.URLField()
    facebook_link = models.URLField()

class Contact_Us(models.Model):
    name  = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()

class Subscription(models.Model):
    email = models.CharField(max_length=255)