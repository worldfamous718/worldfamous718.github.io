#
# World McCrea
# Wake Tech Compute Programming with Python
# 6/26/2024
# This code creates an access key protected file

def main():
    attempts = 0  # setting a blank counter for attempts
    while attempts < 3:  # setting max number of attempts to 3
        if check_access_key(attempts) and attempts < 3:  # set conditions for file access
            process_file()  # grant access to file
            break  # end program once file is accessed successfully
        attempts += 1  # set the counter


def check_access_key(attempts=0):  # function to check how many attempts are made
    access_key = 357  # key for access. I want to figure a way to encrypt this key if possible

    key_try = int(input('Enter your 3 digit access key: '))

    if key_try == access_key:  # set condition for file access
        return True
    else:  # set condition for access denial loop 3 attempts max

        attempts += 1
        if attempts < 3:
            print(f'Incorrect access key. Attempt {attempts + 1}/3. Please try again.')
            return False  # denial condition
        else:
            denials = 0  # I need to fix to this to work after the file closes
            print('You lack clearance for this file!')
            denials += 1
            print(f'Access denied {denials} x:')
            return False






def process_file():
    # function to run the file if access granted
    try:
        with open('example.txt', 'r') as file1:  # my preferred method to open a file
            for line in file1:
                components = line.strip().split(',')  # break the file down by line
                for i in components:  # decode the secret messages
                    if i == 'Boseball':
                        print("Baseball, is code for study functions ")
                    elif i == 'Brondy':
                        print('Brandy, means 2 hours of coding per day')
                    elif i == 'Pathon':
                        print('Python, is a valuable tool if you use it')
                    elif i == 'Fox':
                        print('Next language to learn is R for Data Science')
                        components.append('Python is my favorite language')  # just throwing this is

                    else:
                        print(f'{i}')  # print the rest of the file besides the secret codes
    except FileNotFoundError:
        print('File not found')



if __name__ == '__main__':  # dunder main lmao, That name is ridiculous.I love it!
    main()
# store attempts in a file
