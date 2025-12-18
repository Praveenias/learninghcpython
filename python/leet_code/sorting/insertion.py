def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        #print(key_item,j)
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            print(array)
        array[j + 1] = key_item
            
    print(array)
    return array

insertion_sort([14,13,15,6,7,1])
