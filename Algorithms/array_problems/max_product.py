def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product

    # Sort the array
    arr.sort()

    # Maximum product can be either:
    # 1. Product of two largest numbers
    # 2. Product of two smallest (possibly negative) numbers
    return max(arr[-1] * arr[-2], arr[0] * arr[1])


# Example usage
arr = [3, 5, -2, 8, -7]
print("Maximum product:", max_product(arr))
