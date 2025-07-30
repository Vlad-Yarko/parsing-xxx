from src.clients.product import ProductClient
from src.enums.kasta import URLEnum


class KastaClient(ProductClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE.value
        )
        
    async def get_products(self, product: str, **params: str) -> str:
        self.endpoint = URLEnum.PRODUCTS.value + product
        self.params = params
        html_data = await self.get()
        return html_data
        
    async def get_product(self, product: str, **params: str) -> str:
        self.endpoint = URLEnum.PRODUCT.value + product
        self.params = params
        html_data = await self.get()
        return html_data
