from unittest import TestCase

from pymenu.menu import SelectorMenu, MultiSelectorMenu, FunctionalMenu
from pymenu.misc import FunctionalOption


class TestCreation(TestCase):

    def test_selector_menu(self):
        with self.assertRaises(ValueError):
            SelectorMenu(['С++'], title='Selector')
        with self.assertRaises(ValueError):
            SelectorMenu(['С++', 'Python'], indicator='', title='Selector')
        with self.assertRaises(ValueError):
            SelectorMenu(['С++', 'Python'], default_index=5, title='Selector')

    def test_multi_selector_menu(self):
        with self.assertRaises(ValueError):
            MultiSelectorMenu(['С++'], title='Selector')
        with self.assertRaises(ValueError):
            MultiSelectorMenu(['С++', 'Python'], indicator='', title='Selector')
        with self.assertRaises(ValueError):
            MultiSelectorMenu(['С++', 'Python'], default_index=5, title='Selector')

    def test_functional_menu(self):
        data = [
            FunctionalOption('test', lambda _x: print(1)),
            FunctionalOption('test2', lambda _x: print(1)),
        ]
        with self.assertRaises(ValueError):
            tmp = [FunctionalOption('test', lambda _x: print(1))]
            FunctionalMenu(tmp, title='Selector')
        with self.assertRaises(ValueError):
            FunctionalMenu(data, default_index=5, title='Selector')
        with self.assertRaises(ValueError):
            FunctionalMenu(data, indicator='', title='Selector')
