from rest_framework import generics, status,views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from cloudinary.exceptions import Error
from users.models import User
from .serializers import ProfileSerializer, LicationSerializer
from .models import Profile,Location

class ProfileView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = ProfileSerializer
    
    def get_object(self):
        user = self.request.user
        profile = Profile.objects.get(user = user)
        # Access all the payment transactions related to the profile
        return profile


    
    def create(self, request, *args, **kwargs):
        try:
            profile = self.get_object()
            serializer = self.get_serializer(profile, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()  # Update the existing profile
        except Profile.DoesNotExist:
            serializer = self.get_serializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()  # Create a new profile
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  
    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        # return Response({"points":str(profile.points),"transactions":str(profile.payments),"pic":serializer.data},status= status.HTTP_200_OK)
        return Response(serializer.data,status= status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.delete()
        return Response({"message":"profile picture removed "},status=status.HTTP_204_NO_CONTENT)
    
    
class LocationView(views.APIView):
    def get (self, request):
        try:
            location = Location.objects.all()
        except Location.DoesNotExist:
            return Response({'detail': 'location not set.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicationSerializer(location,many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)
        
        
    def post(self,request):
        serializer = LicationSerializer(data=request.data)
        user = self.request.user
        profile = Profile.objects.get(user = user)
        
        if serializer.is_valid():
            serializer.data['userProfile'] = profile
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"warning":"an error occured"},status=status.HTTP_400_BAD_REQUEST)
    

            
            
            
            
            
            
            