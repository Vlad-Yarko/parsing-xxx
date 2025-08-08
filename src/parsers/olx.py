from src.parsers.product import ProductParser
from src.sequences import ProductSequence


class OLXParser(ProductParser):
    def __init__(
        self,
        olx_sequence: ProductSequence
        ):
        super().__init__(
            sequence=olx_sequence
        )
