from backends.pools.cart import CartPool
from cart.models import Cart
from core.exceptions import ValidationError, ModelDoesNotFound


class CartIntegration:

    @classmethod
    def cart_add_patch(
        cls, cart, products
    ):
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

        return cart

    @classmethod
    def cart_get_or_create(cls, user, supermarket):
        if not supermarket:
            raise ValidationError('Por favor informe o mercado')

        backend = CartPool.get('cart_backend')
        cart, products = backend.create_or_get_cart(user, supermarket)

        return cart, products

    @classmethod
    def cart_delete(cls, user):
        backend = CartPool.get('cart_backend')
        backend.delete_cart(user)

        return
