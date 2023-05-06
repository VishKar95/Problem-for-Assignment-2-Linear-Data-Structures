def kth_smallest_largest_sort(arr, k):
    # find kth smallest number
    arr.sort()
    kth_smallest = arr[k-1]
    
    # find kth largest number
    arr.sort(reverse=True)
    kth_largest = arr[k-1]
    
    return kth_smallest, kth_largest
arr = [5, 3, 9, 1, 7]
k = 3
kth_smallest, kth_largest = kth_smallest_largest_sort(arr, k)
print(kth_smallest)  # output: 5
print(kth_largest)   # output: 5

import heapq

def kth_smallest_largest_heap(arr, k):
    # find kth largest number
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    for x in arr[k:]:
        if x > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, x)
    kth_largest = min_heap[0]
    
    # find kth smallest number
    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)
    for x in arr[k:]:
        if x < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -x)
    kth_smallest = -max_heap[0]
    
    return kth_smallest, kth_largest
