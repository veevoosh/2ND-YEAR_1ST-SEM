# Activity 4

# Credits: DataCamp

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

# Credits: GeeksForGeeks
    
    def delete_value(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            while (temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
            if (temp == None):
                return
            prev.next = temp.next
            temp = None

# Credits: DataCamp

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    L_list = LinkedList()

    L_list.prepend(4)
    L_list.prepend(10)
    L_list.prepend(3)
    L_list.prepend(2)
    L_list.prepend(1)
    L_list.traverse()
    print()
    
    L_list.append(5)
    L_list.append(10)
    L_list.append(15)
    L_list.traverse()
    print()
    
    L_list.delete_value(10)
    
    # Credits: GeeksForGeeks
    
    print(">> Linked List after Deletion of 10:")
    L_list.traverse()
    print()
