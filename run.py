from pymenu.menu import SelectorMenu


def main() -> None:
    ans = SelectorMenu(['С++', 'Python', 'Pascal'], title='Выбери ЯП мечты').input()
    print(ans)


if __name__ == "__main__":
    main()
