from abc import ABC
from curses import KEY_UP, KEY_DOWN, KEY_ENTER
from typing import NamedTuple, Callable


class Option(NamedTuple):
    """
    :param name: name of chosen item in a menu
    :param index: index of chosen item in a menu.
    """
    name: str
    index: int


class FunctionalOption(NamedTuple):
    """
    :param name: name of option
    :param func: func of option, will be return after a functional menu.
    """
    name: str
    func: Callable


class Keyboard(ABC):
    UP = (KEY_UP, ord('w'))
    DOWN = (KEY_DOWN, ord('s'))
    APPROVE = (KEY_ENTER, ord('\n'))
    SELECT = (ord(' '),)
