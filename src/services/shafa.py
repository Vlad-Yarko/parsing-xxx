from src.services.product import ProductService
from src.clients import ShafaClient
from src.parsers import ShafaParser


class ShafaService(ProductService):
    def __init__(self):
        super().__init__(
            client=ShafaClient(),
            parser=ShafaParser()
        )
