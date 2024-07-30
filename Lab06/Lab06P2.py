#
# World McCrea
# 6/11/24
# This program test my knowledge of Tuples. I pronounce it Tupples, lol

import random
def main():
    # Ask user for how many values in the tuple
    print('Step a:')
    values = int(input('How many values to put in the tuple? '))

    # Ask user for start and end values
    print('Step b:')
    start = int(input('What is the start of the range? '))
    end = int(input('What is the end of the range? '))

    # Generate random integers using a loop
    rand_ints = [] # using a list first, will convert to tuple
    for i in range(values):
        rand_ints.append(random.randint(start, end))
    rand_tuple = tuple(rand_ints)
    print(f'Step c: Tuple of {values} random numbers: {rand_tuple}')

    # create a new tuple with first four elements
    first_four = rand_tuple[:4]
    print(f'Step d: Tuple or the first 4 numbers: {first_four} ')

    # create a new tuple with the last 2 numbers from rand_tuple
    last_two = rand_tuple[-2:]
    print(f'Step e: Tuple of 2 last numbers: {last_two}')

    # Concatenated list
    dual_tupe = last_two + first_four
    print(f'Two tuples concatenated: {dual_tupe}')

    # Add 1 from all elements in tuple and display
    # Im  using a list and  list comprehension

    new_tuple = tuple(element + 1 for element in dual_tupe) # this method is amazing
    print(f'Step g: Two tuples concatenated and incremented {new_tuple} ')

    # yesssss it worked!!!!!













main()
