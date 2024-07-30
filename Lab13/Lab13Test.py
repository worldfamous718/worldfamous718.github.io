#
# World
# 7/11/2024
# Test area for lab


# this code can be used as guess the day of the week
from datetime import date, time, datetime

# prompt user to input date
user_input = input('Enter a date (e.g mm/dd/yyyy):')

try:
    # convert input into datetime object
    user_date = datetime.strptime(user_input, '%m/%d/%Y')

    week_day = user_date.strftime('%A')
    print(f'That date was on a {week_day}.')
except ValueError:
    print('Date in wrong format')
