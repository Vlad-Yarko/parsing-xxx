from src.parsers.product import ProductParser
from src.sequences import ProductSequence


class ShafaParser(ProductParser):
    def __init__(
        self,
        shafa_sequence: ProductSequence
        ):
        super().__init__(
            sequence=shafa_sequence
        )
