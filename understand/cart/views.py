import logging

from decimal import Decimal
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from backends.pools.cart import CartPool
from cart.models import Cart
from cart.serializers import CartSerializer
from core.exceptions import ModelDoesNotFound, ValidationError
from products.serializers import ProductSerializer

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
        if not supermarket:
            raise ValidationError('Por favor informe o mercado')

        backend = CartPool.get('cart_backend')
        cart, products = backend.create_or_get_cart(user, supermarket)

        return JsonResponse(
            {
                "cart_id": cart.id,
                "user": cart.user.email,
                "finish": cart.finish,
                "supermarket": cart.supermarket.name,
                "products": products
            }
        )

    def delete(self, request, format=None):
        user = request.auth.user
        backend = CartPool.get('cart_backend')
        backend.delete_cart(user)
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

        if not products:
            raise ValidationError(_('Sem produtos na lista'))

        if not cart:
            raise ValidationError(_('Por favor informe o carrinho'))

        try:
            cart = Cart.objects.get(pk=cart)
        except Cart.DoesNotExist:
            raise ModelDoesNotFound(detail=_('Carrinho informado é invalido'))

        backend = CartPool.get('cart_backend')
        cart = backend.add_products_to_cart(cart, products)

        return JsonResponse(
            CartSerializer(cart).data
        )
