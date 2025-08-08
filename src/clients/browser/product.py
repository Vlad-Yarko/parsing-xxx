from abc import abstractmethod

from playwright.async_api import Playwright

from src.utils.client import BrowserClient
from src.clients.product import ProductClient


class ProductClientBrowser(ProductClient, BrowserClient):
    def __init__(
        self,
        p: Playwright,
        context_page_url: str,
        context_file_name: str
    ):
        super().__init__(
            p=p,
            browser_quantity=3,
            context_amount_per_one_b=5,
            page_amount_pew_one_c=20,
            headless=False,
            context_page_url=context_page_url,
            context_file_name=context_file_name
        )
    
    
    @abstractmethod
    async def get_products(self, *args, **kwargs) -> str:
        raise NotImplementedError()
        
    @abstractmethod
    async def get_product(self, *args, **kwargs) -> str:
        raise NotImplementedError()
