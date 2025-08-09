from src.sequences.product import ProductSequence


class OLXSequence(ProductSequence):
    products_window = "div > form > div > div > div > div > div"  
    products_title = "div > div > div > a > h4"
    products_price = "div > div > div > p"
    product_window = ""
    product_title = ""
    product_price = ""
