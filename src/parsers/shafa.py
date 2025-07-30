from src.parsers.product import ProductParser
from src.sequences import ShafaSequence


class ShafaParser(ProductParser):
    def __init__(self):
        super().__init__(
            sequence=ShafaSequence()
        )
