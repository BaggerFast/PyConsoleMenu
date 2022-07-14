from pymenu import MultiSelectorMenu, FunctionalOption, SelectorMenu, FunctionalMenu


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
