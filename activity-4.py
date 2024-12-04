class Stack: 
    # Initialize stack
    def __init__(self):
        # Insert elements manually
        self.stack = ['Kris', 'Susie', 'Ralsei', 'Noelle', 'Berdly']

    # Credits: GeeksforGeeks

    def recursive_reverse(self, stack):
        # Initialize stack argument
        self.stack = stack
        # Set stack as 'for_reverse' variable for reversal
        for_reverse = self.stack
        # Use reverse() method to reverse the order of the stack
        for_reverse.reverse()
        # Return the reversed stack
        return for_reverse

# Instantiate the Stack() class
stack = Stack()

# Test for stack

# Display stack before reversal
print(f"\n>> Stack before reverse: {stack.stack}")

# Set reversed stack as 'reversed' varaible for output formatting
reversed = stack.recursive_reverse(stack.stack)
# Display stack in string format after reversal
print(f"\n>> Stack after reverse: {str(reversed)}")
# Print a new line for output formatting
print()
