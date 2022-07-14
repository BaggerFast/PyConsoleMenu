from abc import ABC
from curses import KEY_UP, KEY_DOWN, KEY_ENTER
from typing import NamedTuple, Final, Callable


class Option(NamedTuple):
    """
    :param name: name of chosen item in menu
    :param index: index of chosen item in menu
    """
    name: str
    index: int


class FunctionalOption(NamedTuple):
    """
    :param name: name of option
    :param func: func of option, will be return after functional menu
    """
    name: str
    func: Callable


class Keyboard(ABC):
    UP: Final = (KEY_UP, ord('w'))
    DOWN: Final = (KEY_DOWN, ord('s'))
    APPROVE: Final = (KEY_ENTER, ord('\n'))
    SELECT: Final = (ord(' '),)
