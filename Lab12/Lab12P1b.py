#
# World McCrea
# 7/9/2024
# Main file for inventory lab
#

from book import Book
from game import Game
from dvd import DVD


def main():
    items = []  # my empty list.
    for i in range(3):
        item_type = int(input('What item type (1-Book, 2-Game, 3-DVD)? '))
        if item_type == 1:
            item = Book('', 0, 0, '')
            item.get_item_input()
        elif item_type == 2:
            item = Game('', 0, 0)
            item.get_item_input()
        elif item_type == 3:
            item = DVD('', 0, 0, '', '')
            item.get_item_input()
        items.append(item)

    for item in items:
        print(item)


if __name__ == '__main__':
    main()
