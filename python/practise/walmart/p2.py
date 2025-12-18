def count_subarrays_with_max_greater_than_k(n, k, arr):
    count = 0
    current_length = 0

    for i in range(n):
        if arr[i] > k:
            # Extend the subarray
            current_length += 1
            count += current_length
        else:
            # Reset subarray count
            current_length = 0

    return count

# Input Handling
n, k = 5,4
arr = [1,6,7,8,9]

# Function Call
result = count_subarrays_with_max_greater_than_k(n, k, arr)
print(result)