from pymenu.menu import SelectorMenu, MultiSelectorMenu, FunctionalMenu
from pymenu.misc import FunctionalItem


def multi_selector():
    menu = MultiSelectorMenu(['С++', 'Python', 'Pascal', 'C#'], count=3, title='Выбери ЯП мечты')
    ans = menu.input()
    print(ans)


def selector():
    menu = SelectorMenu(['С++', 'Python', 'Pascal'], title='Выбери ЯП мечты')
    ans = menu.input()
    print(ans)


def func1():
    print('Я попугай')


def func2():
    print('Я чебурашка')


def functional():
    data = [
        FunctionalItem('Чебурашка', func1),
        FunctionalItem('Попугай', func2),
    ]
    menu = FunctionalMenu(data, title='Выбери ЯП мечты')
    ans = menu.input()
    ans()


def main() -> None:
    selector()
    # multi_selector()
    # functional()


if __name__ == "__main__":
    main()
