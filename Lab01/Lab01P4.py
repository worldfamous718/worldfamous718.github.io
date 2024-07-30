#
# World McCrea
# 5/22/2024
# Program to calculate customer invoices for Bargain Swap Shop.
#

# inventory item prices (in USD)
book_price = 2.25
dvd_price = 4.35
games_price = 5.00

# get amount of books purchased (input)
total_books = int(input("Enter the number of books: "))
# get subtotal of books purchased
book_subtotal = book_price * total_books

# get amount of DVD's purchased
total_dvds = int(input("Enter the number of DVD's: "))
# get subtotal of DVD's purchased
dvds_subtotal = dvd_price * total_dvds

# get amount of games purchased
total_games = int(input("Enter the number of games: "))
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

# come back later and figure out how to align the decimal points for higher customer input
# these field widths only work for low number inputs. Higher numbers misalign decimal points.
# there has to be a way and I WILL figure it out. -specify minimum field width
# print(f'Subtotal: ${subtotal:9.2f}\nSales tax: ${sales_tax:8.2f}\nGrand total: ${grand_total: .2f} ')
