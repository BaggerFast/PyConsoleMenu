import curses
from abc import ABC
from curses import wrapper, use_default_colors, curs_set
from typing import List, Callable
from pymenu.misc import Item, Keyboard, FunctionalItem


class __BaseMenu(ABC):

    def __init__(self, options: list, title: str = '', default_index: int = 0, indicator: str = "->"):
        if len(options) == 0:
            raise Exception('must contains 1 element')
        if 0 <= default_index >= len(options):
            raise ValueError('default_index should be less than the length of options')
        if not len(indicator):
            raise Exception
        self._title = title
        self._options = options
        self._index = default_index
        self._indicator = indicator
        self._scroll_top = 0

        self._config = {
            Keyboard.UP: self.go_up,
            Keyboard.DOWN: self.go_down,
        }
        self._returnable_config = {
            Keyboard.ENTER: self.get_selected
        }
        self._titles = self._get_titles()

    # region Ideal

    def go_up(self):
        self._index = (self._index - 1) % len(self._options)

    def go_down(self):
        self._index = (self._index + 1) % len(self._options)

    def input(self):
        return wrapper(self.run_loop)

    def _get_titles(self):
        return self._options

    def get_selected(self):
        raise NotImplementedError

    def run_loop(self, screen):
        use_default_colors()
        curs_set(0)
        while True:
            self.draw(screen)
            key = screen.getch()
            for keys in self._config.keys():
                if key in keys:
                    self._config[keys]()
                    break
            for keys in self._returnable_config.keys():
                if key in keys:
                    return self._returnable_config[keys]()

    # endregion

    def draw(self, screen) -> None:
        screen.clear()

        max_y, max_x = screen.getmaxyx()

        y = 0

        for line in self._title.split('\n'):
            screen.addnstr(y, 0, line, max_x)
            y += 1

        for local_y, line in enumerate(self._title):
            if local_y == self._index:
                line = f'{self._indicator}{line}'
            else:
                line = f'{" " * len(self._indicator)}{line}'
            screen.addnstr(y, 0, line, max_x)
            y += 1

        screen.refresh()


class SelectorMenu(__BaseMenu):

    def __init__(self, options: List[str], title: str = '', default_index: int = 0, indicator: str = "->"):
        super().__init__(options, title, default_index, indicator)

    def get_selected(self) -> Item:
        return Item(name=self._options[self._index], index=self._index)


class MultiSelectorMenu(__BaseMenu):

    def __init__(self, options: List[str], count: int, title: str = '', default_index: int = 0, indicator: str = "->"):
        if 1 <= count > len(options):
            raise Exception
        self.count = count
        self.selected: list[int] = []
        super().__init__(options, title, default_index, indicator)
        self._config.update({
            Keyboard.SELECT: self.select
        })

    def select(self):
        if self._index in self.selected:
            self.selected.remove(self._index)
            return
        if len(self.selected) < self.count:
            self.selected.append(self._index)

    def get_selected(self) -> list[Item]:
        self.selected.sort()
        return [Item(index=i, name=self._options[i]) for i in self.selected]

    def draw(self, screen) -> None:
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        screen.clear()

        max_y, max_x = screen.getmaxyx()

        current_line = len(self._title.split('\n'))

        if current_line <= self._scroll_top:
            self._scroll_top = 0
        elif current_line - self._scroll_top > max_y:
            self._scroll_top = current_line - max_y

        lines_to_draw = self._titles[self._scroll_top:self._scroll_top + max_y]

        for y, line in enumerate(lines_to_draw):
            if y - len(self._title.split('\n')) in self.selected:
                screen.addnstr(y, 0, line, max_x - 2, curses.color_pair(1))
                continue
            screen.addnstr(y, 0, line, max_x - 2)
            y += 1

        screen.refresh()


class FunctionalMenu(__BaseMenu):

    def __init__(self, options: List[FunctionalItem], title: str = '', default_index: int = 0, indicator: str = "->"):
        super().__init__(options, title, default_index, indicator)

    def get_selected(self) -> Callable:
        return self._options[self._index].func

    def _get_titles(self):
        return [option.name for option in self._options]
