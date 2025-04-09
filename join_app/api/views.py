from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer
from join_app.models import Users
from rest_framework import mixins
from rest_framework import generics

class UsersView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)