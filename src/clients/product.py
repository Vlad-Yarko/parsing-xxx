from enum import Enum
from typing import Union
from abc import ABC, abstractmethod

from src.utils.client import HTMLClient


class ProductClient(ABC, HTMLClient):
    def __init__(
        self,
        base_url: str,
        URLEnum: Enum
    ):
        super().__init__(
            base_url=base_url
        )
        self.URLEnum = URLEnum
    
    @abstractmethod
    async def get_products(self) -> None:
        raise NotImplementedError()
        
    @abstractmethod
    async def get_product(self) -> None:
        raise NotImplementedError()
