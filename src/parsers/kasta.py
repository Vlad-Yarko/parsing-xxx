from src.parsers.product import ProductParser
from src.sequences import ProductSequence


class KastaParser(ProductParser):
    def __init__(
        self,
        kasta_sequence: ProductSequence
        ):
        super().__init__(
            sequence=kasta_sequence
        )
