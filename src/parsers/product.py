import bs4

from src.utils.parser import Parser
from src.sequences import ProductSequence


class ProductParser(Parser):
    def __init__(
        self,
        sequence: ProductSequence
        ):
        self.sequence = sequence
    
    def get_products(html: str) -> list[dict]:
        pass
    
    def get_product(html: str) -> dict:
        pass
