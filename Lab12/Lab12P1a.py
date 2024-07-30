
#
# World McCrea
# 7/9/2024
# 1st Main file for inventory
#

from  book import Book
from  game import Game
from dvd import DVD

def main():  # this is how the book shows.
    # create 5 objects
    book1 = Book('Python Now', 100, 22.95, '2345234523451')
    book2 = Book('Even More Python', 150, 8.95, '3456345634561')
    game1 = Game('Uno', 75, 6.95)
    dvd1 = DVD('Barbie', 50, 12.00, '098765432121', 'Drama')
    dvd2 = DVD('The Piano', 10, 2.90, '321321321321', 'Drama')

    # Print the objects directly
    print(book1)
    print(book2)
    print(game1)
    print(dvd1)
    print(dvd2)

main()


# # I feel this way is more Pythonic and shows more of my skills
# # less lines of code
# # Im using a list since anything can go in a list
# # I can create the instances of the objects in my list
# # then I can iterate through the whole list of objects and print
# from book import Book
# from game import Game
# from dvd import DVD
#
# # Create a list of instances
# def main():
#     items = [
#         Book("Python Now", 100, 22.95, "2345234523451"),
#         Book("Even More Python", 150, 8.95, "3456345634561"),
#         Game("Uno", 75, 6.95),
#         DVD("Barbie", 50, 12.00, "098765432121", "Comedy"),
#         DVD("The Piano", 10, 2.90, "321321321321", "Drama")
#     ]
#
#     # Iterate over the list and print each item
#     for item in items:
#         print(item)
# if __name__ == '__main__':  # more Pythonic way to call main
#



