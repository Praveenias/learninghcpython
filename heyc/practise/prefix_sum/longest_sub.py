def product_except_self(arr):
    n = len(arr)
    res = [1] * n

    # Compute prefix product directly in res[]
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    # Compute suffix product on the fly and multiply with res[]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res

# Example usage
arr = [1, 2, 3, 4]
print(product_except_self(arr))  