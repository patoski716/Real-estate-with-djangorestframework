from rest_framework import serializers

from .models import Realtor,Listing,Contact


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        read_only_fields = (
            'created_at',
        ),
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'description',
            'image',
            'created_at',  
        )

class ListingSerializer(serializers.ModelSerializer):
    # realtor = serializers.StringRelatedField()
    realtor_name = serializers.CharField(source='realtor.name')
    realtor_email = serializers.EmailField(source='realtor.email')
    realtor_phone = serializers.CharField(source='realtor.phone')
    realtor_image = serializers.ImageField(source='realtor.image')




    class Meta:
        model = Listing
        read_only_fields = (
            'created_at',
            
        ),
        fields = (
            'id',
            'slug',
            'name',
            'realtor',
            'parking_spot',
            'realtor_email',
            'realtor_name',
            'realtor_phone',
            'realtor_image',
            'cover_image',
            'rooms',
            'bathroom',
            'status',
            'location',
            'price',
            'photo_1',
            'photo_2',
            'photo_3',
            'created_at',
        )

    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        read_only_fields = (
            'created_at',
        ),
        fields = (
            'listing',
            'name',
            'email',
            'phone',
            'message',
            'created_at',  
        )