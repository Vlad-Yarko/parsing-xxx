from abc import ABC, abstractmethod

from src.utils.client import HTMLClient


class ProductClient(HTMLClient, ABC):
    @abstractmethod
    async def get_products(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_product(self) -> None:
        raise NotImplementedError()
