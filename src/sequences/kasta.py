from src.sequences.product import ProductSequence


class KastaSequence(ProductSequence):
    products_window = "body > div > div > div > div > div > div > div > div > div > div > div > div > div > div"  
    products_title = "article > div > div > form > div > div > div > a > header"
    products_price = "article > div > div > form > div > div > div > div > div > div > div"
    product_window_s = "body > div > div > div > div > div > div > div > div > div > div > div > form"
    product_title_s = "h1"
    product_price_s = "div > div > div > div"
