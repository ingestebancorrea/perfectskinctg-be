from rest_framework.response import Response
from rest_framework import views,status
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserModifiedView(views.APIView):
    def put(request, pk=None):
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid:
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED) 
            
        return Response(user_serializer.errors)