from rest_framework.response import Response
from rest_framework import views,status
from rest_framework.permissions import IsAuthenticated
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserModifiedView(views.APIView):
    def put(request, pk=None):
        user = User.objects.filter(id = pk).first() #queryset++
        user_serializer = UserSerializer(user, data = request.data)
        permission_classes = (IsAuthenticated,)
        
        if user_serializer.is_valid:
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK) 
            
        return Response(user_serializer.errors, status = status.HTTTP_400_BAD_REQUEST)