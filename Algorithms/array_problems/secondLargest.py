def second_largest(arr):
    first = second = float('-inf')

    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x

    return second if second != float('-inf') else None

