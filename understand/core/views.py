import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from backends.extensions.many_list import ManyToManyRelated
from backends.pools.many_list import ManyListPool
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
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def supermarket_list(request, pk):
    """
    List specific products off a supermarket.
    """
    backend = ManyListPool.get('common_many_to_many')
    response = backend.list_related(Supermarket, pk)
    paginator = Paginator(response['products'], 10)
    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    serializer = ProductSerializer(response, many=True)
    return Response(serializer.data)
