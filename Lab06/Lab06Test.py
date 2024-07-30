

#	Write a list comprehension with both list1 and list2 as input sequences to generate this list:

['4@2', '4@5', '4@9', '5@2', '5@5', '5@9', '8@2', '8@5', '8@9', '2@2', '2@5', '2@9']


list1 = [4, 5, 8, 2]
list2 = [2, 5, 9]

list7 = []

for i in list1:
	for j in list2:
		list7.append(i * j - 1)
print(list7)


#list = [f'{i}@{j}' for i in list1 for j in list2 ]
#print(list6)

