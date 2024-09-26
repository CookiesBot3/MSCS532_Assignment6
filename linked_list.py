class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node by value
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return "Node not found"
        previous.next = current.next

    # Traverse the list and print its elements
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':
    # Example usage
    ll = SinglyLinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.traverse()  # Output: 10 -> 20 -> 30 -> None
    ll.delete(20)
    ll.traverse()  # Output: 10 -> 30 -> None
