# users/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User


# Sign-Up View to handle user registration
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            user = serializer.save()
            token = serializer.get_tokens(user)
            return Response({'token': token}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# 3. Develop API endpoints to add and list users. 
# 4. Develop API endpoints to update and delete a user.
# UserViewSet for handling CRUD operations on users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # For add permission if needed

# Also we can use
# generics.ListCreateAPIView & generics.RetrieveUpdateDestroyAPIView For Add,Update & Delete