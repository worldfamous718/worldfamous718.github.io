#
# World McCrea
# 6/11/24
# This program tests my knowledge of list comprehension
#
def main():
    list1 = [4, 5, 8, 2]
    list2 = [2, 5, 9]

    list3 = []
    for num in range(6):
        list3.append(num * 2 - 3)

    list3 = [num * 2 - 3 for num in range(6)]
    print(f'Step b: {list3} ')

    list4 = []
    for i in range(4):
        for j in range(5):
            if i % 2 == 1 and j % 2 == 0:
                list4.append([i, j])
    list4 = [[i, j] for i in range(4) for j in range(5) if i % 2 == 1 and j % 2 == 0]
    print(f'Step c:{list4} ')

    list5 = []
    for i in list1:
        list5.append(i ** 3)
    list5 = [i ** 3 for i in list1]
    print(f'Step d: {list5} ')

    new_list = []
    new_list = [i * 3 for i in list1]
    print(f'Step e: {new_list}' )

    # I have absolutely no idea what step f or g is even asking for.
    # A lab walkthrough was very necessary for this lab. Pretty unfair.







main()