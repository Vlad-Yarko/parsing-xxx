from src.parsers.product import ProductParser
from src.sequences import OLXSequence


class OLXParser(ProductParser):
    def __init__(self):
        super().__init__(
            sequence=OLXSequence()
        )
