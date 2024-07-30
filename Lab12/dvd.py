#
# World McCrea
# 7/9/2024
# dvd file for inventory
#

from inventory_item import InventoryItem

class DVD(InventoryItem):
    def __init__(self, item_name, item_count, unit_cost, upc, genre):
        super().__init__(item_name, item_count, unit_cost, 'DVD')
        self.upc = upc
        self.genre = genre

    def get_item_input(self):
        super().get_item_input()
        while True:
            upc = input('Enter the UPC: ')
            if len(upc) == 12 and upc.isdigit():
                self.upc = upc
                break
            else:
                print('UPC must be a 12 digit number.')
        self.genre = input('Enter the genre: ')

    def __str__(self):
        result = f"{self.name}\n" + \
                 f"\tCount: {self.count}, Cost: {self.cost:.2f}\n" + \
                 f"\tCategory: {self.category}\n" + \
                 f"\tUPC: {self.upc}\n" + \
                 f"\tGenre: {self.genre}"
        return  result

