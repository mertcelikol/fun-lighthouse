class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def __repr__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return " -> ".join(result)


ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(2)
ll.append(7)
print(ll)