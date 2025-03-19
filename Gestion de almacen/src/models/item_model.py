from models.category_model import Category
from models.placement_model import AilePosition


class Item():
    def __init__(self, name: str, category: Category,min_stock:int, expiration_date:str):
        self.name = name
        self.category = category
        self.min_stock = min_stock
        self.expiration_date = expiration_date



