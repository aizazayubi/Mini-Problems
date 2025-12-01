# def max_product(arr):
#     if len(arr) < 2:
#         return None  # Not enough elements to form a product
#
#     # Sort the array
#     arr.sort()
#
#     # Maximum product can be either:
#     # 1. Product of two largest numbers
#     # 2. Product of two smallest (possibly negative) numbers
#     return max(arr[-1] * arr[-2], arr[0] * arr[1])
#
#
# # Example usage
# arr = [3, 5, -2, 8, -7]
# print("Maximum product:", max_product(arr))
def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    # Initialize the two largest and two smallest values
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        # Update largest values
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Update smallest values
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return max(max1 * max2, min1 * min2)


# Example usage
arr = [3, 5, -2, 8, -7]
print("Maximum product:", max_product(arr))
