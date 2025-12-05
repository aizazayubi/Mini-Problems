# def next_greater_elements(arr):
#     n = len(arr)
#     result = [-1] * n
#     stack = []  # will store indices
#
#     for i in range(n - 1, -1, -1):
#         while stack and arr[stack[-1]] <= arr[i]:
#             stack.pop()
#
#         if stack:
#             result[i] = arr[stack[-1]]
#
#         stack.append(i)
#
#     return result
#
#
# # Example
# arr = [4, 5, 2, 25]
# print(next_greater_elements(arr))  # [5, 25, 25, -1]
#----------------------------------------------------------------
#---------BRUTE FORCE --------------------------------------
#----------------------------------------------------------------
def next_greater(arr):
    n = len(arr)
    result = []

    for i in range(n):
        next_big = -1
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                next_big = arr[j]
                break
        result.append(next_big)

    return result



arr = [4, 5, 2, 25]
print(next_greater(arr))  # [5, 25, 25, -1]
