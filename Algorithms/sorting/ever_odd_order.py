

# even in the right , odd in the left
# def custom_sort(arr):
#     evens = sorted([x for x in arr if x % 2 == 0])
#     odds = sorted([x for x in arr if x % 2 != 0], reverse=True)
#     return evens + odds
#
# # Example


# print(custom_sort(arr))
#
# #another solution
def custom_sort_linear(arr):
    evens = []
    odds = []
    for x in arr:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    return evens + odds

arr = [7, 2, 9, 4, 3, 8]
print(custom_sort_linear(arr))
