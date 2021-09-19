
"""
implementing linked list
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        if self.head is None:
            print("LinkedList is empty")
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->>' if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)
        return

    def insert_at_end(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def print_nodes(self):
        itr = self.head
        while itr:
            print(str(itr))
            itr = itr.next

    def see_pointers(self):

        pointers = list()
        itr = self.head
        while itr:
            pointers.append(str(itr.next))
            itr = itr.next
        for pointer in pointers:
            print(pointer)

    def detect(self):
        count = 0
        itr = self.head
        while itr and count < 1000:
            if itr.next is None:
                loop = "Loop Not Found"
                print(loop)
                return
            count += 1
            itr = itr.next



if __name__ == '__main__':
    listlinki = LinkedList()
    listlinki.insert_at_beginning(1)
    listlinki.insert_at_beginning(85)
    listlinki.insert_at_beginning(100)
    listlinki.insert_at_end(1000)

    # listlinki.print()
    # listlinki.see_pointers()
    listlinki.detect()
