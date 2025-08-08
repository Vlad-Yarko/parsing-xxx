from src.services.product import ProductService
from src.clients import ProductClient
from src.parsers import ProductParser


class ShafaService(ProductService):
    def __init__(
        self,
        shafa_client: ProductClient,
        shafa_parser: ProductParser
        ):
        super().__init__(
            client=shafa_client,
            parser=shafa_parser
        )
