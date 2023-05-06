class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_alternate(head1, head2):
    curr1 = head1
    curr2 = head2
    prev1 = None
    
    while curr1 and curr2:
        # insert node of second list after node of first list
        next1 = curr1.next
        curr1.next = curr2
        prev1 = curr2
        curr2 = curr2.next
        prev1.next = next1
        curr1 = next1
    
    return head1
# create the first linked list
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# create the second linked list
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

# merge at alternate positions
new_head = merge_alternate(head1, head2)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next
