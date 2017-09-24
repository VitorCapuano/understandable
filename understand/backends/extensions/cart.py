import logging
import simplejson

from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from ramos.mixins import ThreadSafeCreateMixin

from backends.cart import CartInterface
from core.exceptions import ModelDoesNotFound
from core.helpers import DecimalEncoder
from products.models import Product
from cart.models import Cart, CartProducts
from supermarket.models import Supermarket

from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class CartBackend(ThreadSafeCreateMixin, CartInterface):
    id = 'cart_backend'

    def delete_cart(self, user):
        try:
            cart = Cart.objects.get(user=user)
            return cart.delete()
        except Cart.DoesNotExist as e:
            raise ModelDoesNotFound('Carrinho inexistente para esse usuário')

    def add_products_to_cart(self, cart, products):
        supermarket = Supermarket.objects.get(pk=cart.supermarket.pk)
        ids_product = []
        [ids_product.append(product.id) for product in supermarket.products.all()]

        for rel in products:
            id_product = rel['id']
            product = Product.objects.get(pk=id_product)
            total_product = rel['qtd'] * product.price
            if not id_product:
                ModelDoesNotFound(detail=_('Por favor informe o ID do produto'))

            if id_product not in ids_product:
                raise ModelDoesNotFound(detail=_('Produto(s) inexistente no mercado'))

            cart_products = CartProducts.objects.filter(cart=cart.pk)

            try:
                cart_products = cart_products.get(product=product)
                cart_products.qtd = rel['qtd']
                cart_products.save()
            except Exception:
                CartProducts.objects.create(
                    cart=cart.pk,
                    product=product,
                    qtd=rel['qtd'],
                    total=total_product
                ).save()

            cart.products.add(product)

        cart.save()

        return cart

    def create_or_get_cart(self, user, supermarket):
        import ipdb; ipdb.set_trace()
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist as e:
            logger.exception('Cart not exist for user {}, exception {}'.format(user, e))
            cart = Cart.objects.create(
                user=user,
                finish=False,
                supermarket=Supermarket.objects.get(pk=supermarket)
            )
            cart.save()

        products = []
        [
            products.append({
                'id': rel.id,
                'name': rel.name,
                'price': rel.price
            })
            for rel in cart.products.all()
        ]

        return cart, products

