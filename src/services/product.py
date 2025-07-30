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
    async def get_products(self) -> list[dict]:
        pass
    
    @http_session
    async def get_product(self) -> dict:
        pass
