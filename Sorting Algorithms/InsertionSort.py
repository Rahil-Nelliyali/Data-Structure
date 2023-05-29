def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        current_element = my_list[i]
        pos = i
        while current_element > my_list[pos - 1] and pos > 0:
            my_list[pos] = my_list[pos - 1]
            pos = pos - 1
        my_list[pos] = current_element


list1 = [123,456,23,45]
insertion_sort(list1)
print(list1)
