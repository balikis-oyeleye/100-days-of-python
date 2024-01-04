
#  # lists: append, insert, pop, remove, clear, index, count
#  # Tuples
#  # unpacking 
#  # dictionaries

x,y,z = 1,2,3
print(x,y,z)

#  exercise

'''
Write a program to find the largest number in a list.
'''

list = [39,9,10,30]

check = list[0]

for number in list:
    if number > check:
        check = number

print(check)

'''
Write a program to remove duplicates from a list
'''

duplicate_list = [1,1,9,5,8,8]
unique_list = []

for number in duplicate_list:
    if number not in unique_list:
        unique_list.append(number)

print(unique_list)