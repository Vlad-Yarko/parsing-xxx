from src.utils.sequence import Sequence


class ProductSequence(Sequence):
    def __init__(self):
        pass
    
    products_window = ""  
    products_title = ""
    products_price = ""
    product_window_s = ""
    product_title_s = ""
    product_price_s = ""
    
    # @property
    # def products_title(self) -> str:
    #     return self.products_window_s + self.products_title_s
    
    # @property
    # def products_price(self) -> str:
    #     return self.products_window_s + self.products_price_s
    
    @property
    def product_title(self) -> str:
        return self.product_window_s + " > " +  self.product_title_s
    
    @property
    def product_price(self) -> str:
        return self.product_window_s + " > " + self.product_price_s
    
