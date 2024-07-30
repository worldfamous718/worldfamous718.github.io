#
# World McCrea
# 7/2/2024
# Trish's Bookstore Inventory System
#
import pickle, textwrap  # I hope we learn about text wrap
CATEGORY_LIST = ['Book', 'DVD', 'Game']

# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":
            item_name, item_count, unit_cost, category = get_item_input()
            # TODO - Replace pass with code that will add the item_name,
            #  item_count, and unit_cost data to the dictionaries
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_categories[item_name] = category


        elif response == "2":  # Display a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will display the item data
            #  from the dictionaries or display "Not found"
            if item_name in inventory_counts:
                print(f'{item_name}\n\tCount: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]:.2f}\n\tCategory: {inventory_categories[item_name]}')
            else:
                print(f'{item_name}: Not Found')

        elif response == "3":  # Display items in a category
            category_name = input('Enter category name: ')
            print(f'\nItems in {category_name}:')
            if category_name in CATEGORY_LIST:
                # TODO - Replace pass with code that will print the names
                #  of all the items in the category
                items_in_category = [name for name in inventory_counts if inventory_categories[name] == category_name]
                print(f'\nItems in {category_name}:')
                for item in items_in_category:
                    print(item)
            else:
                print(f'{category_name} not in list of categories: {CATEGORY_LIST}')

        elif response == "4":  # Delete a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will remove the item data
            #  from the dictionaries or display "Not found"
            if item_name in inventory_counts:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_categories[item_name]
                print(f'{item_name} deleted')
            else:
                print(f'{item_name}" Not Found')
        elif response == "5":  # Display all inventory
            # TODO - Replace pass with code that will display all the inventory
            #  items - HINT Don't we already have a function that does that?
            display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

        elif response != "0":
            print("Invalid choice. Try again.\n")
        print()

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    save_inventory_file(inventory_counts, inventory_costs, inventory_categories)


def display_menu():
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")


def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    # TODO - Replace pass with code that will iterate through the dictionaries
    #  that are passed in and display the inventory. If the dictionaries are
    #  empty the display "== Empty =="
    if len(inventory_counts) == 0:
        print("== Empty ==")
    else:
        # Using textwrap.dedent to fix the gapping issues I keep having
        header = textwrap.dedent("""
                    Item name      Count   Unit Cost  Category
                    ---------      -----   ---------  --------
                    """).strip()  #  this is using the dedent function from textwrap mod

        print(header)  # I learned text wrapping from w3 school python course
        for item in inventory_counts:
            # Format each line with fixed-width fields
            print("{:<14} {:<7} {:<11.2f} {}".format(
                item,
                inventory_counts[item],
                inventory_costs[item],
                inventory_categories[item]))  # I need to practice formatting more. Python Devs should know this!


def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    # TODO - Replace pass with code that will save your dictionaries to
    #  inventory.dat using the pickle module.
    with open('inventory.dat', 'wb') as file:
        pickle.dump((inventory_counts, inventory_costs,inventory_categories), file)



def read_inventory_file():
    inventory_counts = {}
    inventory_costs = {}
    inventory_categories = {}
    # TODO - Replace pass with code that will read your dictionaries from
    #  inventory.dat using the pickle module.
    try:
        with open('inventory.dat', 'rb') as file:
            inventory_data = pickle.load(file)
            return inventory_data
    except FileNotFoundError:
        return inventory_counts, inventory_costs, inventory_categories


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    item_name = input('Enter the item name: ')
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be an integer.')
    # Get category
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
