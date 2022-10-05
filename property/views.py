from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.response import Response

from .models import Realtor,Listing,Contact
from .serializers import RealtorSerializer,ListingSerializer,ContactSerializer
from rest_framework import generics,status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

# public

class RealtorList(generics.ListAPIView):
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()

class ListingList(generics.ListAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Listing, slug=item)

class ContactCreate(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


# admin

class CreateRealtor(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer_class = RealtorSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateListing(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer_class = ListingSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactList(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

