from typing import Optional

from src.utils.client import HTMLClient
from src.clients.product import ProductClient
from src.enums.kasta import URLEnum


class KastaClient(ProductClient, HTMLClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value
        )
        
    async def get_products(self) -> list[dict]:
        return []
    
    async def get_product(self) -> Optional[dict]:
        return None
