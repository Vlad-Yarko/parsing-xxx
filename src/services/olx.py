from src.services.product import ProductService
from src.clients import OLXClient
from src.parsers import OLXParser


class OLXService(ProductService):
    def __init__(self):
        super().__init__(
            client=OLXClient(),
            parser=OLXParser()
        )
