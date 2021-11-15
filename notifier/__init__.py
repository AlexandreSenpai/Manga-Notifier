import sys

from .lib.sources.source import Source
from .lib.workers.sentinel import Sentinel

__all__ = ['sources']
__version__ = '0.0.1'

package_name = "manga-notifier"
python_major = "3"
python_minor = "7"

try:
    assert sys.version_info >= (int(python_major), int(python_minor))
except AssertionError:
    raise RuntimeError(f"\033[31m{package_name!r} requires Python {python_major}.{python_minor}+ (You have Python {sys.version})\033[0m")


Notifier = Source
Sentinel = Sentinel
