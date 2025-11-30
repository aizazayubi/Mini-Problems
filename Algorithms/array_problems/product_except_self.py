def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [0] * n

    # Build left products
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    # Build right products
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    # Multiply left and right products
    for i in range(n):
        result[i] = left[i] * right[i]

    return result

# Example
print(product_except_self([1, 2, 3, 4]))
