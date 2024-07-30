#
# World McCrea
# 7/9/2024
# book file for inventory.
#

from inventory_item import InventoryItem


class Book(InventoryItem):
    def __init__(self, item_name, item_count, unit_cost, isbn13):
        super().__init__(item_name, item_count, unit_cost, 'Book')
        self.isbn13 = isbn13

    def get_item_input(self):
        super().get_item_input()
        while True:
            isbn13 = input('Enter the ISBN13: ')
            if len(isbn13) == 13 and isbn13.isdigit():
                self.isbn13 = isbn13
                break
            else:
                print('ISBN13 must be a 13 digit number. ')

    def __str__(self):
        return f"{self.name}\n" + \
            f"\tCount: {self.count}, Cost: {self.cost:.2f}\n" + \
            f"\tCategory: {self.category}\n" + \
            f"\tISBN: {self.isbn13}"

