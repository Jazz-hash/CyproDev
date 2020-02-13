from .serializers import ProfileModelSerializer
from rest_framework import generics
from rest_framework import permissions
from accounts.models import Profile


class ProfileUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProfileModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
