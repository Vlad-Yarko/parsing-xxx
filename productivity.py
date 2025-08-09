import asyncio

from playwright.async_api import async_playwright

from src import (
    OLXService,
    ShafaService,
    KastaService
)
from src.clients.browser import OLXClient, ShafaClient, KastaClient
from src.parsers import OLXParser, ShafaParser, KastaParser
from src.sequences import OLXSequence, ShafaSequence, KastaSequence


OLX_PRODUCTS_MOCK = "кросівки"
OLX_PRODUCT_MOCK = "krosvki-hoka-x-satisfy-clifton-ls-black-premium-IDXfEc2.html"

SHAFA_PRODUCTS_MOCK = "кросівки"
SHAFA_PRODUCT_MOCK = "uk/women/zhenskaya-obuv/krossovki/190295220-zhenskie-firmennye-krossovki-guess"

KASTA_PRODUCTS_MOCK = "кросівки"
KASTA_PRODUCT_MOCK = "19855269:584"


async def main() -> None:
    p = await async_playwright().start()
    
    olx_service = OLXService(
        olx_client=OLXClient(p),
        olx_parser=OLXParser(olx_sequence=OLXSequence())
    )
    shafa_service = ShafaService(
        shafa_client=ShafaClient(p),
        shafa_parser=ShafaParser(shafa_sequence=ShafaSequence())
    )
    kasta_service = KastaService(
        kasta_client=KastaClient(p),
        kasta_parser=KastaParser(kasta_sequence=KastaSequence())
    )
    
    # Start browsers
    # await olx_service.get_products(OLX_PRODUCTS_MOCK)
    # await shafa_service.get_products(SHAFA_PRODUCTS_MOCK)
    await kasta_service.get_products(KASTA_PRODUCTS_MOCK)
    
    productivity_tasks = asyncio.gather(
        # olx_service.get_products(OLX_PRODUCTS_MOCK),
        # olx_service.get_product(OLX_PRODUCT_MOCK),
        # shafa_service.get_products(SHAFA_PRODUCTS_MOCK),
        # shafa_service.get_product(SHAFA_PRODUCT_MOCK),
        # kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        # kasta_service.get_product(KASTA_PRODUCT_MOCK),
        # olx_service.get_products(OLX_PRODUCTS_MOCK),
        # olx_service.get_product(OLX_PRODUCT_MOCK),
        # shafa_service.get_products(SHAFA_PRODUCTS_MOCK),
        # shafa_service.get_product(SHAFA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK),
        kasta_service.get_products(KASTA_PRODUCTS_MOCK),
        kasta_service.get_product(KASTA_PRODUCT_MOCK)
    )
    
    await productivity_tasks
    
    await p.stop()
    
    
if __name__ == '__main__':
    asyncio.run(main())
