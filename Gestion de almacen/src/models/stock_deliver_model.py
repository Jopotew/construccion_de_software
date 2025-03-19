from models.item_model import Item
from time import sleep


class DeliverStock:
    """
    Class representing a stock delivery with item, quantity, stock location, and status.
    """

    def __init__(self, item: Item, quantity: int, status: bool = False):
        """
        Initialize a DeliverStock instance.

        :param item: Item object representing the product.
        :param quantity: Integer indicating the quantity to deliver.
        :param status: Boolean indicating if the delivery is completed (default is False).
        """
        self.item = item
        self.quantity = quantity
        self.status = status

    # Getter for item
    def get_item(self) -> Item:
        """
        Get the item of the delivery.

        :return: Item object.
        """
        return self.item

    # Getter for quantity
    def get_quantity(self) -> int:
        """
        Get the quantity of items to deliver.

        :return: Integer quantity.
        """
        return self.quantity

    # Getter for status
    def get_status(self) -> bool:
        """
        Get the delivery status.

        :return: Boolean status.
        """
        return self.status
    

    def make_order(self):
        print("Se ha realizado un pedido de {self.item.name} por una cantidad de {self.quantity}")
        sleep(5)
        print("El pedido ha sido entregado")
        return self.get_quantity()

