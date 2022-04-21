from .myfirstlibrary import MyFirstLibrary
from importlib.metadata import version

try:
    __version__ = version("robotframework-myfirstlibrary")
except Exception:
    pass