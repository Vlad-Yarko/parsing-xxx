import enum


class URLEnum(str, enum.Enum):
    BASE = "https://shafa.ua/"
    PRODUCTS = "clothes" # is invalid
    PRODUCT = "" # invalid
