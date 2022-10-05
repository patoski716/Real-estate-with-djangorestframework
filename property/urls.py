from django.urls import path
from .views import *

urlpatterns = [
    path('realtors/', RealtorList.as_view(), name='realtorlist'),
    path('listings/', ListingList.as_view(), name='listinglist'),
    path('listings/<str:pk>/', ListingDetail.as_view(), name='detail'),
    path('createrealtor/', CreateRealtor.as_view(), name='createrealtor'),
    path('createlisting/', CreateListing.as_view(), name='createlisting'),
    path('createcontact/', ContactCreate.as_view(), name='createcontact'),
    path('viewcontact/', ContactList.as_view(), name='viewcontact'),





]