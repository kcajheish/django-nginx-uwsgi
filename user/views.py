from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from user.serializers import GroupSerializer, UserSerializer
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    key_pattern = 'user:%s'
    #permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        user_key = self.key_pattern % pk
        user_data = cache.get(user_key)
        if user_data:
            return Response(user_data)
        queryset = User.objects.get(pk=pk)
        serializer = self.serializer_class(
            instance=queryset,
            context={
                'request': request
            }
        )
        user_data = serializer.data
        cache.set(user_key, user_data, 100)
        return Response(user_data)




class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]
