from typing import Optional

from bs4 import BeautifulSoup, Tag 


# This class is not used directly for parsing, only for inherence

class Parser:
    def __init__(
        self,
        parse_engine: str = 'lxml'
        ):
        self.parse_engine = parse_engine
    
    def parse_by_inheritance_group(self, html: str, sequence: str) -> list[Tag]:
        soup = BeautifulSoup(html, self.parse_engine)
        elements = soup.select(sequence)
        return elements
    
    def parse_one_by_inheritance(self, html: str, sequence: str) -> Optional[Tag]:
        soup = BeautifulSoup(html, self.parse_engine)
        element = soup.select_one(sequence)
        return element
