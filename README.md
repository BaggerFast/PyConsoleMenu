# PyConsoleMenu
![Language](https://img.shields.io/badge/Language-Python3.7+-blue.svg?style=flat)
[![BUILD-STATUS](https://github.com/BaggerFast/Snake/workflows/CI/badge.svg)](https://github.com/BaggerFast/Snake/actions?query=workflow%3Aci)

A simple Python menu in the terminal using curses. 
Ideal for people who want to quickly make a menu without writing their own complicated crutches. 
Includes: SelectorMenu, MultipleSelectorMenu, FunctionalMenu

## Installation 💾
- using pip
```
$ pip install py_menu_console
```

- using GitHub *(требуется [git](https://git-scm.com/downloads))*
```
$ git clone https://github.com/BaggerFast/PyConsoleMemu
$ cd PyConsoleMemu
$ pip install -r requirements.txt
```

## Usage example ⌨️
```py
from py_menu_console import MultiSelectorMenu, FunctionalOption, SelectorMenu, FunctionalMenu


def multi_selector():
    menu = MultiSelectorMenu(['Cheburashka', 'Parrot', 'Snake', 'Gena'], title='MultiSelector', count=3)
    ans = menu.input()
    print(ans)


def selector():
    menu = SelectorMenu(['Cheburashka', 'Parrot', 'Snake', 'Gena'], title='Selector')
    ans = menu.input()
    print(ans)


def functional():
    data = [
        FunctionalOption('Cheburashka', lambda _: print('I am a Parrot')),
        FunctionalOption('Parrot', lambda _: print('I am a Cheburashka')),
    ]
    menu = FunctionalMenu(data, title='Functional')
    ans = menu.input()
    ans()
```
*[See more examples](https://github.com/BaggerFast/PyConsoleMenu/tree/main/examples)*

**Was written in these videos on YouTube 👀** \
[Video#1](https://www.youtube.com/watch?v=wgK90PIzlng&t=118s) \
[Stream#1](https://www.youtube.com/watch?v=7eHcjkM-mTs&t=6046s) \
[Stream#2](https://www.youtube.com/watch?v=ppZoCcmPhpc&t=2941s)

