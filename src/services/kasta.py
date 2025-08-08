from src.services.product import ProductService
from src.clients import ProductClient
from src.parsers import ProductParser


class KastaService(ProductService):
    def __init__(
        self,
        kasta_client: ProductClient,
        kasta_parser: ProductParser
        ):
        super().__init__(
            client=kasta_client,
            parser=kasta_parser
        )
