#
# World McCrea
# 7/9/2024
# Game file for inventory
#
from inventory_item import InventoryItem


class Game(InventoryItem):
    def __init__(self, item_name, item_count, unit_cost, upc=None):
        super().__init__(item_name, item_count, unit_cost, 'Game')
        self.upc = upc

    def get_item_input(self):
        super().get_item_input()
        while True:
            upc = input('Enter the UPC: ')
            if len(upc) == 12 and upc.isdigit():
                self.upc = upc
                break
            else:
                print('UPC must be a 12 digit number.')

    def __str__(self):
        result = f"{self.name}\n" + \
                 f"\tCount: {self.count}, Cost: {self.cost:.2f}\n" + \
                 f"\tCategory: {self.category}"
        if self.upc:
            result += f"\n\tUPC: {self.upc}"
        return result
