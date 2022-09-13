from rest_framework.response import Response
from rest_framework import generics
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserModifiedViews(generics.RetrieveAPIView):
    def delete(request, pk=None):
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid:
            user_serializer.save()
            return Response(user_serializer.data) 
            
        return Response(user_serializer.errors)