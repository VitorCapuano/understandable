import logging

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication
from rest_framework.exceptions import  ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from backends.pools.cart import CartPool
from cart.models import Cart
from core.exceptions import ModelDoesNotFound
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
        Return a cart uuid
        """
        user = request.auth.user
        supermarket = request.query_params.get('supermarket')

        backend = CartPool.get('common_many_to_many')
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


class ProductsToCart(APIView):
    """
    View to Create Cart
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
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

        backend = CartPool.get('common_many_to_many')
        cart = backend.add_products_to_cart(cart, products)

        return JsonResponse(
            {
                "cart_id": cart.id,
                "user": cart.user.email,
                "finish": cart.finish,
                "products": [
                    ProductSerializer(p).data for p in cart.products.all()
                ]
            }
        )
