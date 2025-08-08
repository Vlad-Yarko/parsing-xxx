from typing import Union, Optional
from enum import Enum

from src.utils.client import HTMLClient
from src.clients.product import ProductClient
from src.enums.shafa import URLEnum


class ShafaClient(ProductClient, HTMLClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value
        )
        self.URLEnum = URLEnum
            
    async def get_products(self, product: str, **filters: Union[str, Enum]) -> Optional[str]:
        self.endpoint = self.URLEnum.PRODUCTS.value
        self.params = filters
        self.params["search_text"] = "+".join(product.split(" "))
        html_data = await self.get()
        return html_data
    
    async def get_product(self, product: str, **filters: Union[str, Enum]) -> Optional[str]:
        # self.endpoint = self.URLEnum.PRODUCT.value
        # html_data = await self.get()
        # return html_data
        pass
