class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# Example usage
s = Stack()
s.push(10)
s.push(20)
print(s.peek())   # 20
print(s.pop())    # 20
print(s.pop())    # 10
print(s.pop())    # None
