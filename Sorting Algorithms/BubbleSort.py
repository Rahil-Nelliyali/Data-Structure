lst = ['anas', 'bob', 'aman', 'vys']


def bubble_sort(list1):
    for j in range(len(list1) - 1):
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

    return list1


print(bubble_sort(lst))
