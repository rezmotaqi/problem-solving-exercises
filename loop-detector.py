"""given head of a linked list, Detecting loop in it"""

def has_cycle(head):
    result = 0

    if head == None:
        return result

    slow = head
    fast = head

    while slow and fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            result = 1
            return result

    return result