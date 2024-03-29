
#   # SEARCHING ALGORITHMS




# The Sequential Search

def sequential_search(list, item):
    found = False
    for i in range(len(list)):
        if list[i] == item:
            found = True
    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search(test_list, 13))


# The Binary Search

def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

test_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list2, 9))