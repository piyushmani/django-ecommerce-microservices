from rest_framework import generics
from userAuth.models import User
from userAuth.serializers import ProfileSerializer



class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    name = 'user-detail'