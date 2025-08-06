class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last


    def reverse(self):
        current = self.head
        temp = None
        
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "\n")
            temp = temp.next
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Original List:")
dll.print_list()

dll.reverse()

print("Reversed List:")
dll.print_list()

