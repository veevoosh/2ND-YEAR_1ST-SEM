class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Credits: Hackers Realm (YouTube)

    def insert_at_position(self, new_data, pos):
        # Create a new node
        new_node = Node(new_data)

        # If head pointer is NULL
        if self.head == None:
            self.head = new_node
        elif pos > 0:
            temp = self.head
            count = 1
            # Skip the node to reach position
            while temp != None and count < pos:
                temp = temp.next
                count += 1
            
            # Credits: Mr. Jel Cyruz Porcopio (CS 201)
            
            # If temp position is invalid
            if temp is None:
                print(f">> Position '{pos}' is invalid.\n")
                
            else:
                # Insert the node
                new_node.next = temp.next
                temp.next = new_node
                    
                # Return the new node
                return self.head

    # Credits: Hackers Realm (YouTube)

    def delete_at_position(self, pos):
        # If position is head node
        if pos == 0:
            self.head = self.head.next
        elif pos > 0:
            temp = self.head
            count = 1
            # Skip the node to reach position
            while temp != None and count < pos:
                temp = temp.next
                count += 1
                
        # Credits: Mr. Jel Cyruz Porcopio (CS 201)

            # If temp position is invalid
            if temp is None:
                print(f">> Position '{pos}' is invalid.\n")
                
            else:
                # Delete the node
                temp.next = temp.next.next

                # Return the new node
                return self.head
    
    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")

dll = DoublyLinkedList()

dll.insert_at_position(5, 0)
dll.insert_at_position(10, 1)
dll.insert_at_position(15, 2)
dll.insert_at_position(12, 2)

print("\nDoubly Linked List after inserting elements:")
dll.display()
print()

dll.delete_at_position(3)

print("Doubly Linked List after deleting from Position 3:")
dll.display()
print()