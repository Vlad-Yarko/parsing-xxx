from abc import ABC, abstractmethod


class ProductClient(ABC):    
    @abstractmethod
    async def get_products(self, *args, **kwargs) -> str:
        raise NotImplementedError()
        
    @abstractmethod
    async def get_product(self, *args, **kwargs) -> str:
        raise NotImplementedError()
