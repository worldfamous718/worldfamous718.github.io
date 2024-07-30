#
# World McCrea
# 6/7/2024
# Lab05 program for Lists

import random
def main():
    #step a
    numbers_in_list = int(input('Step a: How many numbers do you want in the list? '))

    #step b
    print('Step b:')
    lower = int(input('choose a lower bound:'))
    upper = int(input('choose an upper bound: '))

    #step c
    list_numbers = []
    for number in range(numbers_in_list):
        number  = random.randint(lower, upper)
        list_numbers.append(number)
    print(f'Step c: First list {list_numbers} ')

    #step d
    list_numbers2 = []
    for number in range(numbers_in_list):
        number = random.randint(lower, upper)
        list_numbers2.append(number)
    print(f'Step d:  Second list {list_numbers2} ')

    #step e, pg 410 in book!
    for blah in range(len(list_numbers, )):
        print('Step e:')
        print('list_numbers[blah], list_numbers2[blah]')


    #step f
    list_numbers3 =list_numbers + list_numbers2
    print(f'Step f: Combined list: {list_numbers3} ')

    #step g
    list_numbers3.sort()
    print(f'Step g: Sorted list: {list_numbers3} ')

    #step h
    print('Step h:')
    print(f'First three elements: {list_numbers3[:3]}')
    print(f'Last three elements: {list_numbers3[-3:]}')
    print(len(list_numbers3))






main()