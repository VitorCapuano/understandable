from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.serializers import ClientSerializer


class ClientList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
