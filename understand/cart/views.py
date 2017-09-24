import logging

from django.http import JsonResponse
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from cart.integration import CartIntegration
from cart.serializers import CartSerializer

logger = logging.getLogger(__name__)


class CreateCart(APIView):
    """
    View to Create Cart
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a cart uuid or create cart
        """
        user = request.auth.user
        supermarket = request.query_params.get('supermarket')

        cart, products = CartIntegration.cart_get_or_create(
            user=user,
            supermarket=supermarket
        )

        return JsonResponse(
            CartSerializer(cart).data
        )

    def delete(self, request, format=None):
        user = request.auth.user
        CartIntegration.cart_delete(user=user)
        return Response(status=HTTP_204_NO_CONTENT)


class ProductsToCart(APIView):
    """
    View to Create Cart
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def patch(self, request, format=None):
        """
        Add products to cart
        """
        cart = request.data.get('cart')
        products = request.data.get('products')

        cart = CartIntegration.cart_add_patch(
            cart=cart,
            products=products
        )

        return JsonResponse(
            CartSerializer(cart).data
        )
