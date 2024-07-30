#
# World McCrea
# 5/30/2024
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
# Keep this clean and simple. Don't overthink!
for month in range(1, 4):
    books += 45
    dvds += 32
    games += 15
    print(f'Month {month}')
    print(f'\t\t\tBooks: {books}')
    print(f'\t\t\t DVDs: {dvds}')
    print(f'\t\t\tGames: {games}')

