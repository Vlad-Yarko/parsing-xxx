from typing import Union, Optional
from enum import Enum

from src.clients.product import ProductClient
from src.enums.shafa import URLEnum


class ShafaClient(ProductClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value,
            URLEnum=URLEnum
        )
            
    async def get_products(self, product: str, **filters: Union[str, Enum]) -> list[dict]:
        self.endpoint = self.URLEnum.PRODUCTS.value
        self.params = filters
        self.params["search_text"] = "+".join(product.split(" "))
        html_data = await self.get()
        return html_data
    
    async def get_product(self, product: str, **filters: Union[str, Enum]) -> Optional[dict]:
        # self.endpoint = self.URLEnum.PRODUCT.value
        # html_data = await self.get()
        # return html_data
        pass
