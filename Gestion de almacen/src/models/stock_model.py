from models.item_model import Item
from models.placement_model import AilePosition
from models.stock_deliver_model import DeliverStock

class Stock:
    """
    Class representing a stock entry that contains an item, its position, and its quantity.
    """

    def __init__(self, item: Item, position: AilePosition, quantity: int):
        """
        Initialize a Stock instance.

        :param item: Item object representing the product stored.
        :param position: AilePosition object representing the location of the item in the stock.
        :param quantity: Integer indicating the quantity of the item in stock.
        """
        self.item = item
        self.position = position
        self.quantity = quantity

    # Getter for item
    def get_item(self) -> Item:
        """
        Get the item stored in stock.

        :return: Item object.
        """
        return self.item

    # Getter for position
    def get_position(self) -> AilePosition:
        """
        Get the position of the item in the stock.

        :return: AilePosition object.
        """
        return self.position

    # Getter for quantity
    def get_quantity(self) -> int:
        """
        Get the quantity of the item in stock.

        :return: Integer quantity.
        """
        return self.quantity


    def decrease_quantity(self, amount: int):
        """
        Decrease the quantity of the item in stock by a specific amount.

        :param amount: Integer amount to decrease.
        :raises ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("The amount to decrease must be greater than zero.")
        if amount > self.quantity:
            self.quantity = 0
        
        if self.quantity == 0:
            pass
        else:
            self.quantity -= amount

        if self.quantity <=  self.item.min_stock:
            self.make_order()
        
        
    def make_order(self):
        stock_deliver = DeliverStock(self.item, 7)
        new_quantity = stock_deliver.make_order()
        quantity += new_quantity