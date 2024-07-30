#
# World McCrea
# 7/9/2024
# Inheritance and Polymorphism - Problem 2
#
import pickle, os
from inventory_item import InventoryItem
from book import Book
from game import Game
from dvd import DVD


def main():
    # Calling load_inventory() should return a list of inventory items if
    # inventory.dat is present. If that file is not present, it should
    # return an empty list.
    inventory = load_inventory()
    display_inventory(inventory)

    answer_outer = ''
    while answer_outer.lower() != 'n':
        answer_inner = ''
        while answer_inner not in ['1', '2', '3']:
            answer_inner = input('What item type (1-Book, 2-Game, 3-DVD)? ')
            if answer_inner not in ['1', '2', '3']:
                print('Enter 1, 2, or 3.')

        # TODO - Create an appropriate object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.
        if answer_inner == '1':  # Book
            name = input('Enter the item name: ')
            count = int(input('Enter the item count: '))
            cost = float(input('Enter the unit cost: '))
            isbn = input('What is the ISBN? ')
            inventory.append(Book(name, count, cost, isbn))
        elif answer_inner == '2':  # Game
            name = input('Enter the item name: ')
            count = int(input('Enter the item count: '))
            cost = float(input('Enter the unit cost: '))
            upc = input('What is the UPC? ')
            inventory.append(Game(name, count, cost, upc))
        elif answer_inner == '3':  # DVD
            name = input('Enter the item name: ')
            count = int(input('Enter the item count: '))
            cost = float(input('Enter the item cost: '))
            upc = input('What is the UPC? ')
            genre = input('What is the genre of the DVD? ')
            inventory.append(DVD(name, count, cost, upc, genre))

        answer_outer = input('Do you want to enter more items? ')

    display_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    inventory = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    inventory = []
    filename = 'inventory.dat'
    if os.path.exists(filename):
        with open(filename, 'rb') as file:  # i need to learn how to open rb an wb at the same time
            inventory = pickle.load(file)


    return inventory

def save_inventory(inventory):
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    filename = 'inventory.dat'
    with open(filename, 'wb') as file:
        pickle.dump(inventory, file)


    print('Inventory.dat file was created.')

def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory)  == 0:
        print('Inventory is empty.')
    else:
        for item in inventory:
            print(item)
    print('-----------------')
    print()


main()

#  Now I have an idea how to write a program for my girls side job goal