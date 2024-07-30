#
# World McCrea
# 7/10/2024
# Program to show my use of sys function

import  sys
import random
def main():
    if len(sys.argv) != 4:
        print('Select 3 numbers to play.')
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    sample = int(sys.argv[3])

    random_list = random.sample(range(start, end + 1), sample)

    print(f'Grabbing {sample} random numbers between {start} and {end}:')
    print(random_list)

main()






