def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted into the sorted part
        j = i - 1     # Index of the last element in the sorted part

        # Move elements of the sorted part that are greater than the key
        # one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position in the sorted part
        arr[j + 1] = key
        print(arr)

# Example usage:
input_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(input_list)
print("Sorted array:", input_list)
