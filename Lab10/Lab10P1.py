#
# World McCrea
# 7/2/2024
# Use dictionary comprehensions
#

def main():
    text = input('Enter a string: ').upper()

    # This code counts the number of vowels in the user input
    # and outputs a dictionary of the results.
    # TODO: The following lines of code can be condensed with a
    #  dictionary comprehension. Comment out the part of the code
    #  which can be condensed and implement it as a comprehension.
    vowels = 'AEIOU'
    # letter_count = {}
    # for letter in text:
    #     if letter in vowels:
    #         letter_count[letter] = text.count(letter)
    # print(f'Vowel Count: {letter_count}')
    letter_count = {letter: text.count(letter) for letter in text if letter in vowels}
    print(f'Vowel Count: {letter_count}') # this is my dictionary comprehension above. I love these.

    # This code determines the vowels that appear the least number
    # of times in the user input and outputs a dictionary of the
    # results.
    # TODO: The following lines of code can be condensed with a
    #  dictionary comprehension. Comment out the part of the code
    #  which can be condensed and implement it as a comprehension.
    # min_count = min(letter_count.values())
    # letter_count_min = {}
    # for key, value in letter_count.items():
    #     if value == min_count:
    #         letter_count_min[key] = value
    # print(f'Letter Min: {letter_count_min}')
    min_count = min(letter_count.values())
    letter_count_min = {key: value for key, value in letter_count.items() if value == min_count}
    print(f'Letter Min: {letter_count_min}')  # Comprehensions are a lot cleaner



main()
