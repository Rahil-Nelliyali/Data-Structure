import random

# LAST ELEMENT AS PIVOT
def quicksort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1.pop()

    items_greater = []
    items_lower = []

    for item in list1:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


# FIRST ELEMENT AS PIVOT
def quicksort_first(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]

    items_greater = []
    items_lower = []

    for item in list1[1:]:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort_first(items_lower) + [pivot] + quicksort_first(items_greater)


# MID ELEMENT AS PIVOT
def quicksort_mid(list1):
    if len(list1) <= 1:
        return list1
    else:
        mid = len(list1) // 2
        pivot = list1[mid]

    items_greater = []
    items_lower = []

    for i, item in enumerate(list1):
        if i != mid:

            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

    return quicksort_mid(items_lower) + [pivot] + quicksort_mid(items_greater)


# RANDOM ELEMENT AS PIVOT
def quicksort_random(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot_index = random.randint(0, len(list1) - 1)
        pivot = list1[pivot_index]

    items_greater = []
    items_lower = []

    for i, item in enumerate(list1):
        if i != pivot_index:

            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

    return quicksort_random(items_lower) + [pivot] + quicksort_random(items_greater)


def quicksort_median(list1):
    if len(list1) <= 1:
        return list1
    else:
        first = list1[0]
        last = list1[-1]
        middle_index = len(list1) // 2
        middle = list1[middle_index]

        # Find the median among the first, last, and middle elements
        pivot = sorted([first, middle, last])[1]

        # Partition the list into elements lower and greater than the pivot
        items_greater = []
        items_lower = []
        for i, item in enumerate(list1):
            if item != pivot:
                if item > pivot:
                    items_greater.append(item)
                else:
                    items_lower.append(item)

        return quicksort_median(items_lower) + [pivot] + quicksort_median(items_greater)
