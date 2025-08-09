# It is just example of working of services, but 

# Need to be created like lifespan manager for serving playwright

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
from src.utils.logger import logger


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
    
    olx_result_products = await olx_service.get_products(OLX_PRODUCTS_MOCK)
    olx_result_product = await olx_service.get_product(OLX_PRODUCT_MOCK)
    
    shafa_result_products = await shafa_service.get_products(SHAFA_PRODUCTS_MOCK)
    shafa_result_product = await shafa_service.get_product(SHAFA_PRODUCT_MOCK)
    
    kasta_result_products = await kasta_service.get_products(KASTA_PRODUCTS_MOCK)
    kasta_result_product = await kasta_service.get_product(KASTA_PRODUCT_MOCK)
    
    logger.info(f"OLX_PRODUCTS: {olx_result_products}")
    logger.info(f"OLX_PRODUCT: {olx_result_product}")
    
    logger.info(f"SHAFA_PRODUCTS: {shafa_result_products}")
    logger.info(f"SHAFA_PRODUCT: {shafa_result_product}")
    
    logger.info(f"KASTA_PRODUCTS: {kasta_result_products}")
    logger.info(f"KASTA_PRODUCT: {kasta_result_product}")
    

    
    await p.stop()
    

    
    
if __name__ == '__main__':
    asyncio.run(main())
    
