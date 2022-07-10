import curses
from curses import wrapper, use_default_colors, curs_set
from typing import List
from pymenu.misc import Item, Keyboard


class SelectorMenu:

    def __init__(self, options: List[str], title: str = '', default_index: int = 0, indicator: str = "->"):
        if len(options) == 0:
            raise Exception('must contains 1 element')
        if 0 <= default_index >= len(options):
            raise ValueError('default_index should be less than the length of options')

        self._options = options
        self._title = title
        self._index = default_index
        self._indicator = indicator
        self._scroll_top = 0

    def get_selected(self) -> Item:
        return Item(name=self._options[self._index], index=self._index)

    def get_option_lines(self):
        lines = []
        for index, option in enumerate(self._options):
            if index == self._index:
                prefix = self._indicator
            else:
                prefix = len(self._indicator) * ' '
            lines.append(f'{prefix} {option}')
        return lines

    def get_lines(self):
        title_lines = self._title.split('\n')
        current_line_y = self._index + len(title_lines) + 1
        lines = title_lines + self.get_option_lines()
        return lines, current_line_y

    def go_up(self):
        self._index = (self._index - 1) % len(self._options)

    def go_down(self):
        self._index = (self._index + 1) % len(self._options)

    def draw(self, screen) -> None:
        screen.clear()

        max_y, max_x = screen.getmaxyx()

        lines, current_line = self.get_lines()

        if current_line <= self._scroll_top:
            self._scroll_top = 0
        elif current_line - self._scroll_top > max_y:
            self._scroll_top = current_line - max_y

        lines_to_draw = lines[self._scroll_top:self._scroll_top + max_y]

        for y, line in enumerate(lines_to_draw):
            screen.addnstr(y, 0, line, max_x - 2)
            y += 1

        screen.refresh()

    def run_loop(self, screen):
        config = {
            Keyboard.UP: self.go_up,
            Keyboard.DOWN: self.go_down,
        }
        returnable_config = {
            Keyboard.ENTER: self.get_selected,
        }
        while True:
            self.draw(screen)
            key = screen.getch()
            for keys in config.keys():
                if key in keys:
                    config[keys]()
                    break
            for keys in returnable_config.keys():
                if key in keys:
                    return returnable_config[keys]()

    def __start(self, screen):
        use_default_colors()
        curs_set(0)
        return self.run_loop(screen)

    def input(self):
        return wrapper(self.__start)


class MultiSelectorMenu(SelectorMenu):

    def __init__(self, options: List[str], count: int, title: str = '', default_index: int = 0, indicator: str = "->"):
        if 1 <= count > len(options):
            raise Exception
        self.count = count
        self.selected: list[int] = []
        super().__init__(options, title, default_index, indicator)

    def run_loop(self, screen):
        config = {
            Keyboard.UP: self.go_up,
            Keyboard.DOWN: self.go_down,
            Keyboard.SELECT: self.select
        }
        returnable_config = {
            Keyboard.ENTER: self.get_selected,
        }
        while True:
            self.draw(screen)
            key = screen.getch()
            for keys in config.keys():
                if key in keys:
                    config[keys]()
                    break
            for keys in returnable_config.keys():
                if key in keys:
                    return returnable_config[keys]()

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

        lines, current_line = self.get_lines()

        if current_line <= self._scroll_top:
            self._scroll_top = 0
        elif current_line - self._scroll_top > max_y:
            self._scroll_top = current_line - max_y

        lines_to_draw = lines[self._scroll_top:self._scroll_top + max_y]

        for y, line in enumerate(lines_to_draw):
            if y - len(self._title.split('\n')) in self.selected:
                screen.addnstr(y, 0, line, max_x - 2, curses.color_pair(1))
                continue
            screen.addnstr(y, 0, line, max_x - 2)
            y += 1

        screen.refresh()