#
# World McCrea
# 7/5/2024
# Classes and OO Programming - Problem 2
# Try to be as Pythonic as possible. Goal is to be a developer
import pickle
from inventory_item import InventoryItem, CATEGORY_LIST


def main():
    inventory = load_inventory()
    display_inventory(inventory)

    answer = ''
    while answer.lower() != 'n':
        # TODO - Create an InventoryItem object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.
        item = InventoryItem('', '', '', '')  # I like that pycharm labels these
        item.get_item_input()
        inventory.append(item)

        answer = input('Do you want to enter more items? ')

    for category in CATEGORY_LIST:
        display_category(category, inventory)

    display_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    inventory = []  # do I need this here? It doesn't serve  purpose
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    try:
        with open('inventory.dat', 'rb') as file:
            inventory = pickle.load(file)
    except FileNotFoundError:
        inventory = []
    return inventory


def save_inventory(inventory):
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    with open('inventory.dat', 'wb') as file:
        pickle.dump(inventory, file)

    print('Inventory was saved in inventory.dat.')


def display_category(category_name, inventory):
    print()
    header = f'Items in {category_name}'
    divider = len(header) * '-'
    print(header)
    print(divider)
    # TODO - Display inventory items that are in the specific category
    #  Both the category name and inventory are passed in as parameters.
    #  If there are no items in the category, print "No items."
    specific_items = [item for item in inventory if item.category == category_name]
    if specific_items:  # checking if list is empty. Not Falsy
        for item in specific_items:
            print(item)
    else:
        print('No items.')


def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if inventory:  # Real Python Truthy conditional
        for item in inventory:
            print(item)
    else:
        print('Inventory is empty.')
    print()

    # professor there is no input validation in this code. There were no instructions to add it. I don't like
    # how it runs. I can fix it, but I don't have time to do it now


main()
