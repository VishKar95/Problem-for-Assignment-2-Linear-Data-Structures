class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_groups(head, k):
    # reverse the first group of size k
    curr = head
    prev = None
    next = None
    count = 0
    while curr and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    
    # recursively reverse remaining nodes
    if next:
        head.next = reverse_groups(next, k)
    
    return prev
# create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# reverse in groups of size 2
new_head = reverse_groups(head, 2)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next
