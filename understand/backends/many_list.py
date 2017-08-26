import abc


class CommonManyToMany(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def list_related(self, model, pk):
        pass
