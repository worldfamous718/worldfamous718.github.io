#
# World McCrea
# 6/28/2024
# Lab09
#
import random
def main():
    # Create 2 empty sets
    set1 = set()
    set2 = set()

    # Generate 8 random integers between 1 and 16 inclusive using the randint function
    # from the random module. Store the random integers in set1
    for num in range(8):
        set1.add(random.randint(1, 16))

    # Display set1
    print("set1:", set1)

    # Create set 2 like set 1 was created
    for num in range(8):
        set2.add(random.randint(1, 16))

    # Display set2
    print("set2:", set2)

    # Perform set operations and display results
    print("\nUnion of set1 and set2:")
    print(set1.union(set2))

    print("\nIntersection of set1 and set2:")
    print(set1.intersection(set2))

    print("\nDifference of set1 and set2:")
    print(set1.difference(set2))

    print("\nSymmetric difference of set1 and set2:")
    print(set1.symmetric_difference(set2))

    # Use set comprehension to select the numbers less than 10 from the union set
    # and store them in a new set. Display this set
    print("\nNumbers less than 10 in the union of set1 and set2:")
    print({num for num in set1.union(set2) if num < 10})  # Im learning alot of new ways to use comprehension!!


main()