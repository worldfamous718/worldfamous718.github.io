#
# World McCrea
# 6/14/24
# Count uppercase letters in a string
#
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    # TODO: Delete the following line, then implement the function as indicated
    #   in the problem specification
    line = line.replace('$NAME', 'World McCrea').replace('$EMAIL', 'amccrea1@my.waketech.edu').replace('$CITY', 'Raleigh')

    # print OG line
    print(f'Original line: {line}')

    # number of characters in updated line
    chars = len(line)
    print(f'The number of characters in updated line is {chars}')

    # count how many times my name appears
    my_name = line.count('World McCrea')
    print(f'Occurences of my name: {my_name}')

    # divide line in half and print
    mid_line = chars // 2 # this should divide the line in half. chars is the length
    front = line[:mid_line] # this slice should display the front half
    back = line[mid_line:] # back half
    print(f'First half of the line: {front}')
    print(f'Second half of line :{back}')

    # print upper and lower case
    print(f'Line in uppercase: {line.upper()}') # these should display upper and lower case
    print(f'Line in lowercase: {line.lower()}')






main()
