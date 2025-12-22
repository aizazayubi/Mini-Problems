def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

# Example
# print(is_balanced("{[()]}"))   # True
# print(is_balanced("{[(])}"))   # False
s = input("Enter brackets string: ")
print(is_balanced(s))
