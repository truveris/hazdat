HazDat Hazardous Data Library
=============================

The HazDat Python library provides a class :code:`Shielding` that protects sensitive data from inadvertent misuse. Things like passwords or social security numbers should be forgotten soon after use, and HazDat enforces it. If you would take precautions with `HAZMAT
<http://en.wikipedia.org/wiki/HAZMAT>`_, Why Not HazDat?™

Usage
-------------

:code:`hazdat.Shielding` prevents accessing the :code:`hazdat` attribute more than once:

.. code:: python

    >>> from hazdat import Shielding
    >>> password = Shielding('1234')
    >>> salted = password.hazdat + 'look, i salted it'
    >>> password.hazdat
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "hazdat/hazdat/shielding.py", line 77, in __getattribute__
        return super().__getattribute__(name)
      File "hazdat/hazdat/shielding.py", line 91, in hazdat
        raise AttributeError(msg) from None
    AttributeError: Attribute 'hazdat' accessed more than once

Also, to avoid unintentionally printing or logging, use :code:`shielded.hazdat.str_once` instead of :code:`str(shielded.hazdat)`.

.. code:: python

    >>> print(Shielding('1234').hazdat)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "hazdat/hazdat/shielding.py", line 39, in __str__
        raise AttributeError(msg.format(type(self).__name__))
    AttributeError: Can't access StrGuarded __str__
    >>> ssn = Shielding('1234')
    >>> hazard = ssn.hazdat
    >>> hazard.str_once
    '1234'
    >>> hazard.str_once
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'str' object has no attribute 'str_once'

Notes
-------------

* HazDat doesn't prevent all access to hazardous data, it just tries to prevent *unintentional* access. You can still assign the hazardous data to a variable and use it with impunity... just don't, please.

Running Tests
-------------

::

    pip install -e .[dev]
    tox

To run without coverage:

::

    tox -e nocover
