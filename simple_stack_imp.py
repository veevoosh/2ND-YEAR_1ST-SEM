# All credits to  Educative (2024)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    stack.push("Stan")
    stack.push("Ford")
    stack.push("Dipper")
    stack.push("Mabel")
    stack.push("Bill")

    print(f">> The stack: {stack.items}\n")
    print(f">> The number of items in the stack are: {stack.size()}\n")
    print(f">> The top value in the stack is: {stack.peek()}\n")

    value_popped = stack.pop()
    print(f">> The value removed from the stack: {value_popped}\n")
    print(f">> The remaining elements in the stack are: {stack.items}\n")
    