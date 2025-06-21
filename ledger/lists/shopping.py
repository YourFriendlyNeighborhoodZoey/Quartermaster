"""Module containing base classes for shopping item entries & lists.
"""
#import [package/module]
from ledger.lists.list import ItemEntry, ItemList

import logging


module_logger = logging.getLogger()


class ShoppingEntry(ItemEntry):
    """Sub-Class of `ItemEntry`, meant to additionally track purchase & expiration data.
    """
    def __init__(self):
        """Constructor for the ShoppingEntry class.
        """
class ShoppingList(ItemList):
    """Sub-class of the `ItemList` class, for lists containing `ShoppingEntry` objects.
    """
    def __init__(self):
        """Constructor for the ShoppingList class.
        """


def main():
    """Module method that's invoked when this file is run directly.
    """
    pass


if __name__ == '__main__':
    main()
else:
    module_logger.info("%s has been succesfully imported!" % __name__)