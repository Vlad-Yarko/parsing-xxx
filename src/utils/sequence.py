from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()
