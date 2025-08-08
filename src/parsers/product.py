from typing import Optional

import bs4

from src.utils.parser import Parser
from src.sequences import ProductSequence


class ProductParser(Parser):
    def __init__(
        self,
        sequence: ProductSequence
        ):
        self.sequence = sequence
    
    def get_products(self, html: str) -> list[dict]:
        parsed_data = self.parse_by_inheritance_group(html, self.sequence.products_window)
        data = list()
        for tag in parsed_data:
            title = tag.select_one(self.sequence.products_title)
            price = tag.select_one(self.sequence.products_price)
            if title and price:
                d = dict()
                d["title"] = title.text
                d["price"] = price.text
                data.append(d)
        return data
    
    def get_product(self, html: str) -> Optional[dict]:
        parsed_data = self.parse_one_by_inheritance(html, self.sequence.product_window)
        if not parsed_data:
            return None
        data = dict()
        data["title"] = parsed_data.select_one(self.sequence.product_title)
        data["price"] = parsed_data.select_one(self.sequence.product_price)
        return data
