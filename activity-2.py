# Note: I used our Stacks PowerPoint Lesson as the guide for creating this activity.

class Stack: 
    # Initialize empty stack.
    def __init__(self):
        # Create an empty stack.
        self.stack = []

    # Add an item to the top of the stack.
    def push(self, item):
        # Add the item to the stack, otherwise add the item to the end of stack if it already contains an element.
        self.stack.append(item)
        # Display element pushed onto the stack.
        print(f"\n>> Pushed '{item}' onto the stack.")
        # Display the current stack.
        print(f"\nThe current stack is {self.stack}")

    # Remove and return the top item from the stack. Ensure the stack is not empty before popping.
    def pop(self):
        # If the stack is empty
        if self.is_empty():
            # Display the condition 'Stack Underflow'
            return "\n>> Stack Underflow"
        # Remove the element at the top of the stack.
        return self.stack.pop()
        
    # Return the top item from the stack without removing it.
    def peek(self):
        # If the stack is empty
        if self.is_empty():
            # Display the condition 'Stack Underflow'
            return "\n>> Stack Underflow"
        # Return the element in the stack with the index of [-1].
        return self.stack[-1]

    # Return True if the stack is empty, otherwise return False.
    def is_empty(self):
        # If the stack is empty
        if len(self.stack) == 0:
            # Return True
            return True
        # If the stack is not empty, return False.
        return False

    # Return the number of elements in the stack.
    def size(self):
        # Print the number of elements in the stack.
        print(f"\nThe size of the stack now is: {len(self.stack)}")  # Print the number of elements in the stack.

# Instantiate the Stack() class
stack = Stack()

# Test for stack

# Push or insert '5' onto the empty stack.
stack.push(5)
# Push or insert '10' onto the stack.
stack.push(10)
# Push or insert '15' onto the stack.
stack.push(15)
# Push or insert '20' onto the stack.
stack.push(20)
# Print a new line for output formatting
print()

# Display the top element of the stack
print(f"\n>> The top item of the stack is '{stack.peek()}'")
# Print a new line for output formatting
print()

# Display pop-ed element from the stack
print(f"\n>> The pop-ed element is '{stack.pop()}'")
# Display the size or the number of elements in the stack.
stack.size()
# Display the current stack.
print(f"\nThe current stack is {stack.stack}")

# Display pop-ed element from the stack
print(f"\n>> The pop-ed element is '{stack.pop()}'")
# Display the size or the number of elements in the stack.
stack.size()
# Display the current stack.
print(f"\nThe current stack is {stack.stack}")
# Print a new line for output formatting
print()  # Print a new line for output formatting