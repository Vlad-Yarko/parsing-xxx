import enum


class URLEnum(str, enum.Enum):
    BASE = "https://www.olx.ua/"
    PRODUCTS = "uk/list/q-"
    PRODUCT = "d/uk/obyavlenie/"
