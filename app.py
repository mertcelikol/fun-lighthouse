from dataclasses import dataclass

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

@dataclass
class Linkedlist:
    node: int
    data: object

ll = Linkedlist(1,2)
print(ll)