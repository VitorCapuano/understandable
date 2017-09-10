from ramos.mixins import ThreadSafeCreateMixin

from backends.many_list import CommonManyToMany
from products.models import Product


class ManyToManyRelated(ThreadSafeCreateMixin, CommonManyToMany):
    id = 'common_many_to_many'

    def list_related(self, model, pk):
        spkt = Product.objects.filter(supermarket=pk).values()
        response = []
        for product in spkt:
            response.append(product)

        return response
