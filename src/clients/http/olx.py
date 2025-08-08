from typing import Union
from enum import Enum

from src.clients.http.product import ProductClientHTTP
from src.enums.olx import URLEnum


class OLXClient(ProductClientHTTP):
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
