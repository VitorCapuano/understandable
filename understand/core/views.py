from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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
    spkt = Supermarket.objects.filter(pk=pk)

    if not spkt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SupermarketSerializer(spkt, many=True)

    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_500_BAD_REQUEST)
