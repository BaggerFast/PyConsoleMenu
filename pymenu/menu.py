from curses import wrapper, use_default_colors, curs_set
from typing import List
from pymenu.misc import Item, Keyboard


class SelectorMenu:

    def __init__(self, options: List[str], title: str = '', default_index: int = 0, indicator: str = "->"):
        if len(options) == 0:
            raise ValueError('must contains 1 element')
        if 0 <= default_index >= len(options):
            raise ValueError('default_index should be less than the length of options')

        self.__options = options
        self.__title = title
        self.__index = default_index
        self.__indicator = indicator
        self.__scroll_top = 0

    def get_selected(self) -> Item:
        return Item(name=self.__options[self.__index], index=self.__index)

    def get_option_lines(self):
        lines = []
        for index, option in enumerate(self.__options):
            if index == self.__index:
                prefix = self.__indicator
            else:
                prefix = len(self.__indicator) * ' '
            lines.append(f'{prefix} {option}')
        return lines

    def get_lines(self):
        title_lines = self.__title.split('\n')
        current_line_y = self.__index + len(title_lines) + 1
        lines = title_lines + self.get_option_lines()
        return lines, current_line_y

    def go_up(self):
        self.__index = (self.__index - 1) % len(self.__options)

    def go_down(self):
        self.__index = (self.__index + 1) % len(self.__options)

    def draw(self, screen) -> None:
        screen.clear()

        max_y, max_x = screen.getmaxyx()

        lines, current_line = self.get_lines()

        if current_line <= self.__scroll_top:
            self.__scroll_top = 0
        elif current_line - self.__scroll_top > max_y:
            self.__scroll_top = current_line - max_y

        lines_to_draw = lines[self.__scroll_top:self.__scroll_top + max_y]

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
