import logging

from django.core.exceptions import ObjectDoesNotExist
from ramos.mixins import ThreadSafeCreateMixin

from backends.cart import CartInterface
from core.exceptions import ModelDoesNotFound
from products.models import Product
from cart.models import Cart
from supermarket.models import Supermarket

from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class CartBackend(ThreadSafeCreateMixin, CartInterface):
    id = 'common_many_to_many'

    def add_products_to_cart(self, cart, products):
        import ipdb; ipdb.set_trace()
        products_ids = []
        supermarket = Supermarket.objects.prefetch_related('products').all()
        supermarket = supermarket.filter(pk=cart.supermarket.pk)

        [products_ids.append(p.id) for p in supermarket.products.all()]
        for product_id in products:
            if product_id not in products_ids:
                raise ModelDoesNotFound(detail=_('Produto(s) inexistente no mercado'))

        for product in products_ids:
            cart.products.add(Product.objects.get(pk=product))

        return cart

    def create_or_get_cart(self, user, supermarket):
        try:
            cart = Cart.objects.get(user=user)
        except ObjectDoesNotExist as e:
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

