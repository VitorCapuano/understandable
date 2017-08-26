from ramos.mixins import ThreadSafeCreateMixin

from backends.many_list import CommonManyToMany
from backends.pools.many_list import ManyListPool


class ManyToManyRelated(ThreadSafeCreateMixin, CommonManyToMany):
    id = 'common_many_to_many'

    def list_related(self, model, pk):
        spkt = model.objects.filter(pk=pk)
        response = {}
        for sa in spkt:
            product = sa.products.values()
            response.update({'products': product})

        return response
