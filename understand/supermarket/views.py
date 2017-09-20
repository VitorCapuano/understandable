import logging

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backends.pools.many_list import ManyListPool
from core.helpers import make_pagination_view
from products.serializers import ProductSerializer
from supermarket.models import Supermarket
from supermarket.serializers import SupermarketSerializer

logger = logging.getLogger(__name__)


class SupermarketList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer


class SupermarketDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer


@api_view(['GET'])
def supermarket_list(request, pk):
    """
    List specific products off a supermarket.
    """
    import pdb; pdb.set_trace()
    logger.info("TACALE PAU")
    backend = ManyListPool.get('common_many_to_many')
    response = backend.list_related(Supermarket, pk)
    page = request.GET.get('page', 1)
    response = make_pagination_view(response, page)

    return Response(response.object_list)
