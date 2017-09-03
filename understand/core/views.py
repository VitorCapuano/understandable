import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from backends.extensions.many_list import ManyToManyRelated
from backends.pools.many_list import ManyListPool
from .helpers import make_pagination_view
from users.permissions import IsUserOrReadOnly
from core.models import *
from .serializers import *
from rest_framework import generics, mixins, viewsets, status


class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupermarketList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer


class SupermarketDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@api_view(['GET'])
def supermarket_list(request, pk):
    """
    List specific products off a supermarket.
    """
    logger.error("TACALE PAU")
    backend = ManyListPool.get('common_many_to_many')
    response = backend.list_related(Supermarket, pk)

    page = request.GET.get('page', 1)
    response = make_pagination_view(response['products'], page)

    serializer = ProductSerializer(response, many=True)
    return Response(serializer.data)
