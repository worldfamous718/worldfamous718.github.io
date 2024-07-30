#
# World McCrea
# 7/5/2024
# My files for the invetory lab

# import my inventory items
from inventory_item import  InventoryItem

def main():
    # create inventory objects
    item1 = InventoryItem('Python for All', 10, 12.95, 'Book')
    item2 = InventoryItem('Barbie', 15, 6.95, 'DVD')
    item3 = InventoryItem('Uno', 32, 4.50, 'Game')

    # print objects
    print(item1)
    print(item2)
    print(item3)

    # Create additional user input item
    item4 = InventoryItem('', '', '', '')
    item4.get_item_input()

    #  print user object
    print(item4)

main()


