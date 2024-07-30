#
# World McCrea
# 6/25/2024
# Lab08 Files and exception handling
#
def main():
    # item list for running totals
    book_total = 0
    dvd_total = 0
    games_total = 0

    # try to open the file with exception handling
    try:
        with open('sales.txt', 'r') as file2:  # ask professor if i can write the infile and outfile at the same time
            line_num = 1  # line counter for errors
            for line in file2:
                components = line.strip().split(',')  # strip out the components into a list
                items = components[1].strip()  # Strip extra spaces around the item name
                prices = components[2].strip()  # Get the prices

                # Convert the price string to a float, handling potential errors
                try:
                    price = float(prices)
                except ValueError:
                    print(f"Error on line {line_num}: Could not convert '{prices}' to price format")
                    continue  # Skip this line and move to the next one

                # add to running totals
                if items == 'Book':
                    book_total += price
                elif items == 'DVD':
                    dvd_total += price
                elif items == 'Game':
                    games_total += price
                else:
                    print(f"Warning on line {line_num}: Unknown item '{items}'")  # Warning

                line_num += 1  # line error counter
    except FileNotFoundError:
        print("File 'sales.txt' not found")
        exit()

    # Create and save the daily report
    with open('daily_report.txt', 'w') as report_file:  # ask professor if this can be done on a single line
        report_file.write(f"Books: ${book_total:.2f}\n")
        report_file.write(f"DVDs: ${dvd_total:.2f}\n")
        report_file.write(f"Games: ${games_total:.2f}\n")

    print("Daily sales report successfully created.")

if __name__ == '__main__':
    main()

#  ask professor how I can define a main with this code
