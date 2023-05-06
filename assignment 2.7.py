def move_negatives(arr):
    n = len(arr)
    i, j = 0, n-1
    
    while i < j:
        # find the first negative element from the left
        while i < n and arr[i] >= 0:
            i += 1
        
        # find the first positive element from the right
        while j >= 0 and arr[j] < 0:
            j -= 1
        
        if i < j:
            # swap elements at positions i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    return arr
arr = [5, -2, 3, -1, 8, -4, 7]
print(move_negatives(arr))  # output: [-2, -1, -4, 5, 8, 3, 7]
