list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


result = []


for i in range(len(list1)):
    sum_result = list1[i] + list2[i]
    result.append(sum_result)


print(result)