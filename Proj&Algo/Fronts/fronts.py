
# front

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def front(self):
        if self.head is None:
            return None
        return self.head.value


# remove front

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def removeFront(self):
        if self.head is None:
            return None
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        return self.head

# add front

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        return self.head


# add to back

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_at_back(head, value):
    new_node = ListNode(value)
    if head is None:
        return new_node
    curr_node = head
    while curr_node.next is not None:
        curr_node = curr_node.next
    curr_node.next = new_node
    return head
