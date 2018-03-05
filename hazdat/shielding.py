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

    @property
    def __wrapped__(self):
        """Block access to __wrapped__."""
        raise AttributeError

    def __getattribute__(self, name):
        """Block access to guarded internals.

        :param name: The attribute name.

        """
        if name == '_self_str_once':
            del self._self_str_once
        return super().__getattribute__(name)

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
        result = super().__getattribute__('_self_str_once')
        del self._self_str_once
        return result


class Shielding:
    """A class that allows access to an object only once.

    The object is accessible via the 'hazdat' attribute. It is wrapped in the
    StrGuarded class to prevent printing, logging, etc the object
    unintentionally.

    """

    __slots__ = '_hazdat'

    def __init__(self, hazdat):
        """Set the shielded object.

        :param hazdat: The object to shield. This will be available as the
            'hazdat' attribute, wrapped in the StrGuarded class.

        """
        super().__setattr__('_hazdat', StrGuarded(hazdat))

    def __getattribute__(self, name):
        """Block access to guarded internals.

        :param name: The attribute name.

        """
        if name == '_hazdat':
            del self._hazdat
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        """Block setting of any attributes."""
        msg = "'{}' object attributes are read-only"
        raise AttributeError(msg.format(self.__class__.__name__))

    @property
    def hazdat(self):
        """Use this to access the shielded object."""
        try:
            result = super().__getattribute__('_hazdat')
        except AttributeError:
            msg = "Attribute 'hazdat' accessed more than once"
            raise AttributeError(msg) from None
        del self._hazdat
        return result