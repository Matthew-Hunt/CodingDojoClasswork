#sll util

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


my_list = SLL()

my_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
my_list.head.next = second_node
second_node.next = third_node

print(my_list.contains(2))
print(my_list.contains(4))


# length

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


my_list = SLL()

my_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
my_list.head.next = second_node
second_node.next = third_node


print(my_list.length())


# display


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

my_list = SLL()

my_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
my_list.head.next = second_node
second_node.next = third_node

print(my_list.display())


# bonus

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def move_min_to_front(head):
    if head is None or head.next is None:
        return head

    min_node = head
    prev_min = None
    current = head

    while current.next is not None:
        if current.next.value < min_node.value:
            min_node = current.next
            prev_min = current
        current = current.next

    if prev_min is None:
        return head

    prev_min.next = min_node.next
    min_node.next = head
    head = min_node

    return head


def move_max_to_back(head):
    if head is None or head.next is None:
        return head

    max_node = head
    prev_max = None
    current = head

    while current.next is not None:
        if current.next.value > max_node.value:
            max_node = current.next
            prev_max = current
        current = current.next

    if max_node.next is None:
        return head

    if prev_max is None:
        head = max_node.next
    else:
        prev_max.next = max_node.next

    current.next = max_node
    max_node.next = None

    return head


head = Node(3)
node1 = Node(5)
node2 = Node(2)
node3 = Node(1)
node4 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


new_head = move_min_to_front(head)
current = new_head
while current is not None:
    print(current.value, end=" ")
    current = current.next

print()

new_head = move_max_to_back(new_head)
current = new_head
while current is not None:
    print(current.value, end=" ")
    current = current.next


