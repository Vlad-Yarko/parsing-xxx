from typing import Union
from enum import Enum

from src.utils.client import HTMLClient
from src.clients.product import ProductClient
from src.enums.olx import URLEnum


class OLXClient(ProductClient, HTMLClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value
        )
        self.URLEnum = URLEnum
        
    async def get_products(self, product: str, **filters: Union[str, Enum]) -> str:
        self.endpoint = self.URLEnum.PRODUCTS.value + product
        self.params = filters
        html_data = await self.get()
        return html_data

    async def get_product(self, product: str) -> str:
        self.endpoint = self.URLEnum.PRODUCT.value + product
        html_data = await self.get()
        return html_data
