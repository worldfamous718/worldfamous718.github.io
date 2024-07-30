#
# World McCrea
# 7/11/2024
# Program using the date and time modules
#

from datetime import date, time, datetime


def main():
    present_time = datetime.now()
    print('The current date/time is:')
    # print(present_time) checking if it even worked

    # format like 07/12/24 06:19:06 PM
    print(present_time.strftime('%m/%d/%y %H:%M:%S %p'))

    # format like Thursday, Jul 12, 2024
    print(present_time.strftime('%A, %b %d, %Y'))

    # format like Thu, July 12, 2024
    print(present_time.strftime('%a, %B %d, %Y'))
    print()

    # prompt user to input date
    user_input = input('Enter a date (e.g mm/dd/yyyy): ')

    try:
        # convert input into datetime object
        user_date = datetime.strptime(user_input, '%m/%d/%Y')

        week_day = user_date.strftime('%A')
        print(f'That date was on a {week_day}.')
    except ValueError:
        print('Date in wrong format')


main()
