from abc import abstractmethod

from src.utils.client import HTMLClient
from src.clients.product import ProductClient


class ProductClientHTTP(ProductClient, HTMLClient):
    @abstractmethod
    async def get_products(self, *args, **kwargs) -> str:
        raise NotImplementedError()
        
    @abstractmethod
    async def get_product(self, *args, **kwargs) -> str:
        raise NotImplementedError()
