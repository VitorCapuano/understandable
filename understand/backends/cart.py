import abc


class CartInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_products_to_cart(self, cart, products):
        pass

    @abc.abstractmethod
    def create_or_get_cart(self, user, supermarket):
        pass
