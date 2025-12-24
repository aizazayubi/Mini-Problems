def missing_number_xor(arr):
    n = len(arr) + 1
    xor_all = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for x in arr:
        xor_all ^= x

    return xor_all



arr = [1, 2, 4, 5]
print(missing_number_xor(arr))  # 3

