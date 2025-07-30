from typing import Union, Optional
from enum import Enum

from src.utils.service import Service
from src.utils.client import http_session
from src.clients import ProductClient
from src.parsers import ProductParser


class ProductService(Service):
    def __init__(
        self,
        client: ProductClient,
        parser: ProductParser
    ):
        self.client = client
        self.parser = parser
    
    @http_session
    async def get_products(self, product: str, **filters: Union[str, Enum]) -> Optional[list[dict]]:
        html_data = await self.client.get_products(product, **filters)
        print("DDDDDD", html_data)
        data = self.parser.get_products(html_data)
        print('AAAAAAAAAAA', data)
        if not data:
            return None
        return data
    
    @http_session
    async def get_product(self, product: str) -> Optional[dict]:
        html_data = await self.client.get_product(product)
        data = self.parser.get_product(html_data)
        return data
