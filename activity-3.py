# Credits: CodeBasics (YouTube)

class Node:
    # Initialize empty node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Credits: GeeksforGeeks

class Stack:
    # Initialize empty head node
    def __init__(self):
        self.head = None

    def push(self, item):
        # Create a new node with given data
        new_node = Node(item)
        # Check if memory allocation for the new node failed
        if not new_node:
            # Display the condition 'Stack Overflow'
            print("\n>> Stack Overflow")
            return
        # Link the new node to the current top node
        new_node.next = self.head
        # Update the top to the new node
        self.head = new_node
        # Display element pushed onto the stack.
        print(f"\n>> Pushed '{item}' onto the stack.")

    def pop(self):
        # If stack is empty
        if self.is_empty():
            # Display the condition 'Stack Underflow'
            print("\n>> Stack Underflow")
        else:
            # Assign the current top to a temporary variable
            temp = self.head
            # Display pop-ed element from the stack
            print(f"\n>> The pop-ed element is '{temp.data}'")
            # Update the top to the next node
            self.head = self.head.next
            # Deallocate the memory of the old top node
            del temp
        
    def peek(self):
        # If stack is not empty, return the top element
        if not self.is_empty():
            return self.head.data
        # If stack is empty
        else:
            # Display the condition 'Stack Underflow'
            print("\n>> Stack Overflow")
            return float('-inf')

    def is_empty(self):
        # If head is None, the stack is empty
        return self.head is None
    
    def size(self): 
        # Initialize count with 0
        count = 0
        # Initialize curr with head of Linked List
        curr = self.head
        # Traverse until reach None
        while curr is not None:
            # Increment count by 1
            count += 1
            # Move pointer to next node
            curr = curr.next
        # Return the total count of nodes
        print(f"\n>> The size of the stack now is: {count}")

# Instantiate the Stack() class
stack = Stack()

# Test for stack

# Push or insert '7' onto the empty stack.
stack.push(7)
# Push or insert '14' onto the stack.
stack.push(14)
# Push or insert '21' onto the stack.
stack.push(21)
# Push or insert '28' onto the stack.
stack.push(28)
# Print a new line for output formatting
print()

# Display the top element of the stack
print(f"\n>> The top element of the stack is '{stack.peek()}'")
# Print a new line for output formatting
print()

# Pop or delete the top element of the stack
stack.pop()
# Display the size or the number of elements in the stack.
stack.size()
# Print a new line for output formatting
print()

# Pop or delete the top element of the stack
stack.pop()
# Display the size or the number of elements in the stack.
stack.size()
# Print a new line for output formatting
print()

# Pop or delete the top element of the stack
stack.pop()
# Display the size or the number of elements in the stack.
stack.size()
# Print a new line for output formatting
print()