# Define the node for the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Define the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end
    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            # Traverse to the last node
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Delete a node from the beginning
    def delete_from_beginning(self):
        # If the list is empty
        if self.head is None:
            print("List is empty. No node to delete.")
        else:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            
            # Free memory of the deleted node
            del temp

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")

# Create a doubly linked list and perform operations
dll = DoublyLinkedList()

# Insert nodes at the end
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("\nDoubly Linked List after inserting elements:")
dll.display()
print()

# Delete node from the beginning
dll.delete_from_beginning()

print("Doubly Linked List after deleting from beginning:")
dll.display()
print()