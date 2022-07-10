from pymenu.menu import SelectorMenu, MultiSelectorMenu


def main() -> None:
    # MultiSelector
    menu = MultiSelectorMenu(['С++', 'Python', 'Pascal'], count=2, title='Выбери ЯП мечты')
    ans = menu.input()
    print(ans)

    # Selector
    menu = SelectorMenu(['С++', 'Python', 'Pascal'], title='Выбери ЯП мечты')
    ans = menu.input()
    print(ans)


if __name__ == "__main__":
    main()
