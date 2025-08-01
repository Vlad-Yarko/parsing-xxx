# It is just example of working of services, but 

import asyncio

from src import (
    OLXService,
    ShafaService,
    KastaService
)
from src.utils.logger import logger


olx_service = OLXService()
shafa_service = ShafaService()
kasta_service = KastaService()


OLX_PRODUCTS_MOCK = "кросівки"
OLX_PRODUCT_MOCK = "krosvki-hoka-x-satisfy-clifton-ls-black-premium-IDXfEc2.html"

SHAFA_PRODUCTS_MOCK = "кросівки"
SHAFA_PRODUCT_MOCK = ""

KASTA_PRODUCTS_MOCK = ""
KASTA_PRODUCT_MOCK = ""


async def main() -> None:
    olx_tasks = asyncio.gather(olx_service.get_products(OLX_PRODUCTS_MOCK)) # , olx_service.get_product(OLX_PRODUCT_MOCK)
    shafa_tasks = asyncio.gather(shafa_service.get_products(SHAFA_PRODUCTS_MOCK)) # , shafa_service.get_product(SHAFA_PRODUCT_MOCK)
    # kasta_tasks = asyncio.gather(kasta_service.get_products(KASTA_PRODUCTS_MOCK), kasta_service.get_product(KASTA_PRODUCT_MOCK))
    
    olx_result = await olx_tasks
    shafa_result = await shafa_tasks
    # kasta_result = await kasta_tasks
    
    # logger.info(f"OLX_PRODUCTS: {olx_result[0]}")
    # logger.info(f"OLX_PRODUCT: {olx_result[1]}")
    
    logger.info(f"SHAFA_PRODUCTS: {shafa_result[0]}")
    # logger.info(f"SHAFA_PRODUCT: {shafa_result[1]}")
    
    # logger.info(f"KASTA_PRODUCTS: {kasta_result[0]}")
    # logger.info(f"KASTA_PRODUCT: {kasta_result[1]}")
    
    
if __name__ == '__main__':
    asyncio.run(main())
    
