#
# World McCrea
# 7/5/2024
# Program to show my learning of OO Programming
#

# creating my inventory.py  file
# Name constants

CATEGORY_LIST = ['Book', 'DVD', 'Game']

class InventoryItem:
    def __init__(self, name, count, cost, category):
        self.name = name
        self.count = count
        self.cost = cost
        self.category = category

    def get_item_input(self):
        self.name = input('Enter the item name: ')
        self.count = input('Enter the item count: ')
        self.cost = input('Enter the unit cost: ')
        self.category = input('Enter the category: ')

    def __str__(self):
        return f'{self.name}\n\tcount: {self.count}, Cost: {self.cost}\nCategory: {self.category}'




