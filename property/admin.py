from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Realtor)
admin.site.register(Listing)
admin.site.register(Contact)

