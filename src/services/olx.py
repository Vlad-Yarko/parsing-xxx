from src.services.product import ProductService
from src.clients import ProductClient
from src.parsers import ProductParser


class OLXService(ProductService):
    def __init__(
        self,
        olx_client: ProductClient,
        olx_parser: ProductParser
        ):
        super().__init__(
            client=olx_client,
            parser=olx_parser
        )
