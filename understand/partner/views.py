from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from partner.models import Partner
from partner.serializers import PartnerSerializer


class PartnerList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
