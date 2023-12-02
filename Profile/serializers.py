from rest_framework import serializers
from .models import Profile, Location
from cloudinary import uploader
from mpesa.models import PaymentTransaction


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Profile
        fields = ('profile_id','user', 'profile_pic', 'points')


    def create(self, validated_data):
        # Save the profile instance
        profile = super().create(validated_data)

        if 'profile_pic' in self.context['request'].data:
            uploaded_image = uploader.upload(self.context['request'].data['profile_pic'])
            profile.profile_pic = uploaded_image['url']
            profile.save()

        return profile
    
class LicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('loc_id','name','userProfile')
        extra_kwarg = {'loc_id':{'read_only': True},'userProfile':{'read_only': True}}
