from typing import Optional

from src.clients.product import ProductClient
from src.enums.kasta import URLEnum


class KastaClient(ProductClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value,
            URLEnum=URLEnum
        )
        
    async def get_products(self) -> list[dict]:
        pass
    
    async def get_product(self) -> Optional[dict]:
        pass
