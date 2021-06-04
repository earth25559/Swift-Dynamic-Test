test_array = [-2, -3, 4, -6, 1, 2, 1, 10, 3, 5, 6, 4]


def get_index(max_val):
    for index, value in enumerate(test_array):
        if(value == max_val):
            return index


def find_index_in_array(arr):
    max_value = arr[0]
    for value in arr:
        if value > max_value:
            max_value = value
    index = get_index(max_value)
    print('The greatest value in the array is', max_value)
    print('The index of the greatest value in the array is', index)
    return index


find_index_in_array(test_array)
