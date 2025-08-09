from typing import Optional

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
        
    def get_products(self, html: str) -> list[dict]:
        parsed_data = self.parse_group_by_inheritance(html, self.sequence.products_window)[2]
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
        title = self.parse_one_by_inheritance(html, self.sequence.product_title)
        price = self.parse_group_by_inheritance(html, self.sequence.product_price)[14]
        if title and price:
            data = dict()
            data["title"] = title.text
            data["price"] = price.text
            return data
        return None
