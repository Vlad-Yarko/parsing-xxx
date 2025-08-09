from src.sequences.product import ProductSequence


class ShafaSequence(ProductSequence):
    products_window = "body > div > div > div > div > div > main > div > div"
    products_title = "div > div > div > footer > div > a"
    products_price = "div > div > div > footer > div > div > p"
    product_window_s = "body > div > div > div > div > div > main > div > section"
    product_title_s = "div > h1"
    product_price_s = "div > div > p"
