from tkinter import N
from typing import Optional
from functools import wraps

from playwright.async_api import async_playwright, Browser

from src.utils.client.client import Client
from src.constants.client import BROWSER_CLIENT_STORAGE, BROWSER_CLIENT_TRACING


class BrowserClient(Client):
    def __init__(
        self,
        headless: bool = True,
        context_page_url: Optional[str] = None,
        context_file_name: str = "",
        device_name: str = "Desktop Chrome",
        tracing_file_name: str = ""
        ):
        self.browser: Browser
        self.headless = headless
        self.context_page_url = context_page_url
        self.device = None
        self.device_name = device_name
        self.context_file_name = context_file_name
        self.tracing_file_name = tracing_file_name
    
    async def open_session(self) -> None:
        async with async_playwright() as p:
            self.browser = await p.chromium.launch(headless=self.headless)
            self.device = p.devices[self.device_name]
            if self.cookie_page_url:
                context = await self.browser.new_context(**self.device)
                page = await context.new_page()
                await self.navigate(page, self.cookie_page_url)
                await context.storage_state(path=)
                await context.close()
                await page.close()
        self.context = None
        self.page = None
                
    async def close_session(self) -> None:
        await self.context.tracing.stop(path=BROWSER_CLIENT_TRACING + self.tracing_name)
        await self.page.close()
        await self.context.close()
        await self.browser.close()
        self.context = None
        self.page = None
        self.browser = None
    
    async def navigate(
        self, 
        page, 
        url: str, 
        wait_until: str = "load") -> None:
        await page.goto(url, wait_until=wait_until)
        
    
def browser_session(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        session_was_already_open = self.client.browser is not None
        if not session_was_already_open:
            await self.client.open_session()
        try:
            return await func(self, *args, **kwargs)
        finally:
            if not session_was_already_open:
                await self.client.close_session()
    return wrapper
