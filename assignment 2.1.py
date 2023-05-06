class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_zero_sum(head):
    # create a hashmap to store cumulative sum and its corresponding node
    hashmap = {}
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    cum_sum = 0
    
    while curr:
        cum_sum += curr.val
        if cum_sum in hashmap:
            # remove nodes between current node and node with same cumulative sum
            remove_node = hashmap[cum_sum].next
            cum_remove = cum_sum + remove_node.val
            while cum_remove != cum_sum:
                del hashmap[cum_remove]
                remove_node = remove_node.next
                cum_remove += remove_node.val
            hashmap[cum_sum].next = curr.next
        else:
            hashmap[cum_sum] = curr
        curr = curr.next
        
    return dummy.next
# create a linked list with sum zero
head = Node(3)
head.next = Node(4)
head.next.next = Node(-7)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(-4)
head.next.next.next.next.next.next = Node(-2)

# delete nodes with sum zero
new_head = delete_zero_sum(head)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next
