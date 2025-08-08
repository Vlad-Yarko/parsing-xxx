from src.parsers.product import ProductParser
from src.sequences import ProductSequence


class ShafaParser(ProductParser):
    def __init__(
        self,
        shafa_parser: ProductSequence
        ):
        super().__init__(
            sequence=shafa_parser
        )
