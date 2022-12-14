from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Realtor(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.TextField(blank=True)
    email=models.EmailField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    image=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    slug = models.SlugField(max_length=250 ,default='')
    name=models.CharField(max_length=200,null=True)
    image=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    rooms=models.IntegerField(default=0)
    bathroom=models.IntegerField(default=0)
    parking_spot=models.IntegerField(default=0)
    status=models.CharField(max_length=200,null=True)
    location=models.TextField(blank=True)
    price=models.CharField(max_length=200,null=True)
    photo_1=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    photo_2=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    photo_3=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email