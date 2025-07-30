from src.services.product import ProductService
from src.clients import KastaClient
from src.parsers import KastaParser


class KastaService(ProductService):
    def __init__(self):
        super().__init__(
            client=KastaClient(),
            parser=KastaParser()
        )
