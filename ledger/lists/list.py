"""Script Docstring
"""
#import [package/module]
import logging

module_logger = logging.getLogger(__name__)


class ItemEntry:
    """Base class for item entries.
    """
    def __init__(self, name: str, quantity: int = 1, **kwargs):
        """Constructor for the ItemEntry class.
        """
        self._name = name
        self._quantity = quantity
        self._note = kwargs.get("note", None)
        self._owner = kwargs.get("owner", None)
    

    @property
    def name(self):
        """Getter for the self._name private attribute.

        Returns:
            str: The string representation for the item's name.
        """
        return self._name
    @name.setter
    def name(self, new_name: str):
        """Setter for the self._name private attribute.

        Args:
            new_name (str): The new string to represent the item's name.

        Raises:
            TypeError: Raised when `new_name` is not a string.
        """
        if not isinstance(new_name, str) and not issubclass(new_name, str):
            raise TypeError("new_name was not an instance/sub-class of type(str).")
        self._name = new_name
    @name.deleter
    def name(self):
        """Deleter for the self._name private attribute.
        Sets the value to an empty string.
        """
        self._name = ''

    @property
    def quantity(self):
        """Getter for the self._quantity private attribute.

        Returns:
            int: The integer representation for the item's [stored/desired] quantity in the related context.
        """
        return self._quantity
    @quantity.setter
    def quantity(self, new_amount: int):
        """Setter for the self._quantity private attribute.

        Args:
            new_amount (int): The new quantity.

        Raises:
            TypeError: Raised when `new_amount` isn't an integer.
            ValueError: Raised when `new_amount` is negative.
        """
        if not isinstance(new_amount, int) and not issubclass(new_amount, int):
            raise TypeError("new_amount was not an instance/sub-class of type(int).")
        if (new_amount < 0):
            raise ValueError("")
        self._quantity = new_amount
    @quantity.deleter
    def quantity(self):
        """Deleter for the self._quantity private attribute.
        Sets the value to 0.
        """
        self.quantity = 0

    @property
    def note(self):
        """Getter for the self._note private attribute.

        Returns:
            str: The string representation for the item's attached note.
        """
        return self._note
    @note.setter
    def note (self, new_note):
        """Setter for the self._note private attribute.

        Args:
            new_note (str): The new string for self._note

        Raises:
            TypeError: Raised when `new_note` is not a string.
        """
        if not isinstance(new_note, str) and not issubclass(new_note, str):
            raise TypeError("new_note was not an instance/sub-class of type(str).")
        self._note = new_note
    @note.deleter
    def note(self):
        """Deleter for the self._owner private attribute.
        Sets the value to an empty string.
        """
        self._note = ''

    @property
    def owner(self):
        """Getter for the self._owner private attribute.

        Returns:
            str: The string representation for the item's owner.
        """
        return self._owner
    #* No Setter; Uncertain what types this input will be, so no type validation.
    @owner.deleter
    def owner(self):
        """Deleter for the self._owner private attribute.
        Sets the value to None.
        """
        self._owner = None


class ItemList:
    """
    """
    def __init__(self, entries: ItemEntry | list | tuple | dict):
        """
        """


def main():
    pass


if __name__ == '__main__':
    main()
else:
    module_logger.info("%s has been succesfully imported!" % __name__)