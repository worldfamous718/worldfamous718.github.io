#
# World McCrea
# 5/31/2024
# Input validation revision for Tara.

# inventory item prices (in USD)
book_price = 2.25
dvd_price = 4.35
games_price = 5.00

# get amount of books purchased (input)
total_books = int(input ("Enter the number of books: "))
while total_books < 0:
    break    #or total_books > 30:
    print('Warning! Zero is the least amount you can choose.')
while total_books > 30:

    print('Note, this item also has a purchase limit of 30.')
    total_books = int(input("Please enter a valid number of books: "))
# get subtotal of books purchased
book_subtotal = book_price * total_books

# get amount of DVD's purchased
total_dvds = int(input("Enter the number of DVD's: "))
while total_dvds < 0 or total_dvds > 15:
    print('Warning! Zero is the least amount you can choose.')
    print('Note, this item also has a purchase limit of 15.')
    total_dvds = int(input("Please enter a valid number of DVD's: "))
# get subtotal of DVD's purchased
dvds_subtotal = dvd_price * total_dvds

# get amount of games purchased
total_games = int(input("Enter the number of games: "))
while total_games < 0 or total_games > 10:
    print('Warning! Zero is the least amount you can choose.')
    print('Note, this item also has a purchase limit of 10. ')
    total_games = int(input('Please enter a valid number of games: '))
# get subtotal of games purchased
games_subtotal = games_price * total_games

# calculate total before tax (processing)
subtotal = book_subtotal + dvds_subtotal + games_subtotal

# calculate sales tax on subtotal (processing)
sales_tax = subtotal * .065

# calculate total after tax (processing)
grand_total = subtotal + sales_tax

# display subtotal, tax, and grandtotal (output)
print(f'Subtotal: ${subtotal: .2f}\nSales tax: ${sales_tax: .2f}\nGrand total: ${grand_total: .2f} ')

