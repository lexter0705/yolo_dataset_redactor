import abc


class Spliterator(abc.ABC):
    @abc.abstractmethod
    def split(self, *args, **kwargs):
        pass