import curses
from typing import Callable, Union
from .base import BaseMenu
from .misc import Option, Keyboard, FunctionalOption


class SelectorMenu(BaseMenu):
    """
    Class for creation selector menu in console

    :param options: a list of options to choose from
    :param title: (optional) a title above options list
    :param default_index: (optional) set this if the default selected option is not the first one
    :param indicator: (optional) customize the selection indicator
    """

    def _get_selected(self) -> Option:
        return Option(name=self._options[self._index], index=self._index)

    def input(self) -> Option:
        """
        Return chosen option as Item
        """
        return super().input()


class MultiSelectorMenu(BaseMenu):
    """
    Class for creation multi selector menu in console

    :param options: a list of options to choose from
    :param title: (optional) a title above options list
    :param default_index: (optional) set this if the default selected option is not the first one
    :param indicator: (optional) customize the selection indicator
    :param count: a number of max chosen options
    """

    def __init__(self, options: list[str], title: str = '',  default_index: int = 0, indicator: str = "->",
                 count: int = None) -> None:

        count = len(options) if not count else count
        if 1 <= count > len(options):
            raise ValueError('Count  must be in [2, len(options)]')

        super().__init__(options, title, default_index, indicator)
        self.__count = count
        self.__selected: list[int] = []
        self._control_config[Keyboard.SELECT] = self.__select

    # region Private

    def __select(self) -> None:
        if self._index in self.__selected:
            self.__selected.remove(self._index)
            return
        if len(self.__selected) < self.__count:
            self.__selected.append(self._index)

    def _draw_options(self, screen, max_x: int) -> None:
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        for local_y, line in enumerate(self._options):
            if local_y == self._index:
                line = f'{self._indicator}{line}'
            else:
                line = f'{" " * len(self._indicator)}{line}'

            if local_y in self.__selected:
                screen.addnstr(self._y, 0, line, max_x, curses.color_pair(1))
            else:
                screen.addnstr(self._y, 0, line, max_x)
            self._y += 1

    def _get_selected(self) -> Union[list[Option], None]:
        if not self.__selected:
            return
        return [Option(index=i, name=self._options[i]) for i in sorted(self.__selected)]

    # endregion

    def input(self) -> list[Option]:
        """
        Return list of chosen options as Items
        """
        return super().input()


class FunctionalMenu(BaseMenu):
    """
    Class for creation functional menu in console

    :param options: a list of options to choose from
    :param title: (optional) a title above options list
    :param default_index: (optional) set this if the default selected option is not the first one
    :param indicator: (optional) customize the selection indicator
    """

    def __init__(self, options: list[FunctionalOption], title: str = '', default_index: int = 0,
                 indicator: str = "->") -> None:

        self.__functions: list[Callable] = []
        local_options: list[str] = []
        for option in options:
            self.__functions.append(option.func)
            local_options.append(option.name)
        super().__init__(local_options, title, default_index, indicator)

    def _get_selected(self) -> Callable:
        return self.__functions[self._index]

    def input(self) -> Callable:
        """
        Return chosen Callable object
        """
        return super().input()
