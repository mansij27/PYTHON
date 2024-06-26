"""Not done by me"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, " -> ", end='')
            temp = temp.next_node
        print("")

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def get_next_node(self, node):
        return node.next_node.data

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    s = Node(2)
    t = Node(3)
    u=Node(4)
    llist.head.next_node = s;
    s.next_node = t
    t.next_node=u
    llist.printList()
    print("s data", s.data)
    print("size is",llist.size())
    print("Next of s",llist.get_next_node(s))
    llist.insert_at_head(5)
    llist.printList()