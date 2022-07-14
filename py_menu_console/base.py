from typing import Any, List
from abc import ABC
from curses import wrapper, use_default_colors, curs_set
import _curses
from .misc import Keyboard


class BaseMenu(ABC):
    """
    Class for creation console menu

    :param options: a list of options to choose from
    :param title: (optional) a title above options list
    :param default_index: (optional) set this if the default selected option is not the first one
    :param indicator: (optional) customize the selection indicator
    """

    def __init__(self, options: List[str], title: str = '', default_index: int = 0, indicator: str = "->") -> None:

        # region parse Exceptions

        if len(options) <= 1:
            raise ValueError('Options must contains > 1 element')
        if 0 <= default_index >= len(options):
            raise ValueError('Default_index must be in [0, len(options)-1]')
        if len(indicator) == 0:
            raise ValueError('Len of indicator must be > 0')

        # endregion

        self._y = 0
        self._title = title
        self._options = options
        self._indicator = indicator
        self._index = default_index
        self._control_config = {
            Keyboard.UP: self._go_up,
            Keyboard.DOWN: self._go_down,
            Keyboard.APPROVE: self._get_selected
        }

    # region Private

    def _go_up(self) -> None:
        self._index = (self._index - 1) % len(self._options)

    def _go_down(self) -> None:
        self._index = (self._index + 1) % len(self._options)

    def _run_loop(self, screen) -> Any:
        use_default_colors()
        curs_set(0)
        while True:
            self._draw(screen)
            key = screen.getch()
            for keys, func in self._control_config.items():
                if key not in keys:
                    continue
                ret = func()
                if ret is not None:
                    return ret

    def _get_selected(self) -> Any:
        raise NotImplementedError

    # region Drawers

    def _draw(self, screen) -> None:
        screen.clear()
        _, max_x = screen.getmaxyx()

        self._y = 0
        try:
            self._draw_title(screen, max_x)
            self._draw_options(screen, max_x)
        except _curses.error:
            raise Exception('This terminal is small to update information')

        screen.refresh()

    def _draw_title(self, screen, max_x: int) -> None:
        if self._title:
            for line in self._title.split('\n'):
                screen.addnstr(self._y, 0, line, max_x)
                self._y += 1

    def _draw_options(self, screen, max_x: int) -> None:
        for local_y, line in enumerate(self._options):
            if local_y == self._index:
                line = f'{self._indicator}{line}'
            else:
                line = f'{" " * len(self._indicator)}{line}'
            screen.addnstr(self._y, 0, line, max_x)
            self._y += 1

    # endregion

    # endregion

    # region Public

    def input(self) -> Any:
        return wrapper(self._run_loop)

    # endregion
