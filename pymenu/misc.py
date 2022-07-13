from abc import ABC
from curses import KEY_UP, KEY_DOWN, KEY_ENTER
from typing import NamedTuple, Final, Callable


class Item(NamedTuple):
    name: str
    index: int


class FunctionalItem(NamedTuple):
    name: str
    func: Callable


class Keyboard(ABC):
    UP: Final = (KEY_UP, ord('w'))
    DOWN: Final = (KEY_DOWN, ord('s'))
    ENTER: Final = (KEY_ENTER, ord('\n'))
    SELECT: Final = (ord(' '),)
