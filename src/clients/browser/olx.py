from typing import Union
from enum import Enum

from playwright.async_api import Playwright

from src.clients.browser.product import ProductClientBrowser
from src.enums.olx import URLEnum
from src.constants.olx import CONTEXT_FILE_NAME


class OLXClient(ProductClientBrowser):
    def __init__(
        self,
        p: Playwright
    ):
        super().__init__(
            p=p,
            context_page_url=URLEnum.BASE.value,
            context_file_name=CONTEXT_FILE_NAME
        )
    
    async def get_products(self, product: str, **filters: Union[str, Enum]) -> str:
        page, context, browser = await self.create_page()
        await page.goto(url=URLEnum.BASE.value + URLEnum.PRODUCTS.value + product, timeout=60000)
        content = await page.content()
        await self.close_page(browser, context, page)
        return content
    
    async def get_product(self, product: str) -> str:
        page, context, browser = await self.create_page()
        await page.goto(url=URLEnum.BASE.value + URLEnum.PRODUCT.value + product, timeout=60000)
        content = await page.content()
        await self.close_page(browser, context, page)
        return content
