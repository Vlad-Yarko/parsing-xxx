import os
from typing import Optional

from playwright.async_api import Playwright, Page, BrowserContext, Browser

from src.utils.client.client import Client
from src.utils.browser_manager import browser_manager
from src.constants.client import BROWSER_CLIENT_STORAGE


class BrowserClient(Client):
    client_type = "browser"
    
    def __init__(
        self,
        p: Playwright,
        browser_quantity: int,
        context_amount_per_one_b: int,
        page_amount_pew_one_c: int,
        headless: bool = True,
        context_page_url: Optional[str] = None,
        context_file_name: str = "",
        device_name: str = "Desktop Chrome",
        tracing_file_name: str = ""
        ):
        self.p = p
        self.browser_quantity = browser_quantity
        self.context_amount_per_one_b = context_amount_per_one_b
        self.page_amount_pew_one_c = page_amount_pew_one_c
        self.browser_manager = browser_manager
        self.headless = headless
        self.device_name = device_name
        self.device = None
        self.context_page_url = context_page_url
        self.context_file_name = context_file_name
        self.tracing_file_name = tracing_file_name
    
    async def open_session(self) -> None:
        self.device = self.p.devices[self.device_name]
        storage_path = BROWSER_CLIENT_STORAGE + self.context_file_name
        for _ in range(self.browser_quantity):
            browser = await self.p.chromium.launch(headless=self.headless)
            self.browser_manager.browsers[browser] = dict()
        if self.context_page_url and self.context_file_name:
            if not os.path.exists(storage_path):
                context = await self.browser_manager.browsers[0].new_context(**self.device)
                page = await context.new_page()
                await page.goto(self.context_page_url)
                await context.storage_state(path=storage_path)
                await context.close()
                await page.close()
        for browser in self.browser_manager.browsers:
            for i in range(self.context_amount_per_one_b):
                context = await browser.new_context(storage_state=storage_path, **self.device)
                # context.tracing.start(screenshots=True, snapshots=True, sources=True)
                self.browser_manager.browsers[context] = list()
                
    async def close_session(self) -> None:
        for browser in self.browser_manager.browsers:
            await browser.close()
        self.device = None
        
    async def create_page(self) -> tuple[Page, BrowserContext, Browser]:
        pass
    
    async def close_page(self) -> None:
        pass
        
