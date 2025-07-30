from src.parsers.product import ProductParser
from src.sequences import KastaSequence


class KastaParser(ProductParser):
    def __init__(self):
        super().__init__(
            sequence=KastaSequence()
        )
