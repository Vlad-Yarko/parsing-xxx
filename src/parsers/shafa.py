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
        
    def get_products(self, html: str) -> list[dict]:
        parsed_data = self.parse_by_inheritance_group(html, self.sequence.products_window)[0]
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
