"""Module containing classes for inventory item entries & lists.
"""
#import [package/module]
from ledger.lists.list import ItemEntry, ItemList

import logging


module_logger = logging.getLogger()


class InventoryEntry(ItemEntry):
    """Sub-Class of `ItemEntry`, meant to additionally track storage & expiration data.
    """
    def __init__(self):
        """Constructor for the InventoryEntry class.
        """
class InventoryList(ItemList):
    """Sub-class of the `ItemList` class, for lists containing `IntentoryEntries` objects.
    """
    def __init__(self):
        """Constructor for the InventoryList class.
        """


def main():
    """Module method that's invoked when this file is run directly.
    """
    pass


if __name__ == '__main__':
    main()
else:
    module_logger.info("%s has been succesfully imported!" % __name__)