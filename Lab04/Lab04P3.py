#
# World McCrea
# 6/4/2024
# Special Dice Game Program
# Use everything I learned and practice stuff too.

# import the random module to use

import random

# Make a main function. Ask professor to please explain this. I don't understand fully
# Use try and except for input validation
def main():
    while True:
        try:
            num_rolls = int(input("How many times do you want to roll the die? "))
            if 5 <= num_rolls <= 15:
                break
            else:
                print("Enter a number between 5 and 15.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    roll_die(num_rolls)
    print("Thanks for playing!")

# make the functions outside of the main scope?
def roll_die(rolls):
    for i in range(1, rolls + 1):
        roll_result = random.randint(1, 20)
        if roll_result == 20:
            print(f"Roll {i}: 20 ==> CRITICAL HIT!")
        else:
            symbol = ""
            if roll_result % 4 == 0:
                symbol = "Sword"
            elif roll_result % 4 == 1:
                symbol = "Shield"
            elif roll_result % 4 == 2:
                symbol = "Spell"
            elif roll_result % 4 == 3:
                symbol = "Potion"
            print(f"Roll {i}: {roll_result} ==> {symbol}")  # Learned this one ==> from TheRealPython

# I have to credit W3 schools for this bit of code. Its not mine. I learned it. For whatever reason I cant call main without it
# It doesn't even really make sense.
#Otherwise I got this! I learned to use try and except and while and else elif. Very happy!
#if __name__ == "__main__":
    main()

# Oh If I move main() to the starting edge, I don't need if __name__ = __main__'