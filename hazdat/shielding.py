"""The Shielding class."""
from wrapt import ObjectProxy


class StrGuarded(ObjectProxy):
    """A wrapper class that prevents access to __str__."""

    def __init__(self, wrapped):
        """Set the wrapped object.

        :param wrapped: The wrapped object.

        """
        super().__init__(wrapped)
        self._self_str_once = super().__str__()

    def __getattribute__(self, name):
        """Block access to guarded internals.

        :param name: The attribute name.

        """
        result = super().__getattribute__(name)
        if name == '_self_str_once':
            del self._self_str_once
        return result

    def __dir__(self):
        """Return the list of attributes."""
        return super().__dir__() + ['str_once']

    def __str__(self):
        """Raise AttributeError."""
        msg = "Can't access {} __str__"
        raise AttributeError(msg.format(type(self).__name__))

    @property
    def str_once(self):
        """Use this to access __str__, but only once."""
        return self._self_str_once


class Shielding:
    """A class that allows access to an object only once.

    The object is accessible via the 'hazdat' attribute. It is wrapped in the
    StrGuarded class to prevent printing, logging, etc the object
    unintentionally.

    """

    __slots__ = 'hazdat'

    def __init__(self, hazdat):
        """Set the shielded object.

        :param hazdat: The object to shield. This will be available as the
            'hazdat' attribute, wrapped in the StrGuarded class.

        """
        super().__setattr__('hazdat', StrGuarded(hazdat))

    def __getattribute__(self, name):
        """Block access to guarded internals.

        :param name: The attribute name.

        """
        result = super().__getattribute__(name)
        if name == 'hazdat':
            del self.hazdat
        return result
