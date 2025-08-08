from playwright.async_api import Playwright

from src.clients.browser.product import ProductClientBrowser
from src.enums.shafa import URLEnum
from src.constants.shafa import CONTEXT_FILE_NAME


class ShafaClient(ProductClientBrowser):
    def __init__(
        self,
        p: Playwright
    ):
        super().__init__(
            p=p,
            context_page_url=URLEnum.BASE.value,
            context_file_name=CONTEXT_FILE_NAME
        )
    
    async def get_products(self) -> str:
        return ""
    
    async def get_product(self) -> str:
        return ""
