"""Public API definitions for HazDat."""
import pkg_resources

from .shielding import Shielding


__all__ = ('Shielding',)
__version__ = pkg_resources.get_distribution('hazdat').version
