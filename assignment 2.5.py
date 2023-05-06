def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    # count frequency of each element in the array
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    
    # find duplicates
    for x in arr:
        if freq[x] > 1 and x not in duplicates:
            duplicates.append(x)
    
    return duplicates
arr = [1, 2, 3, 1, 4, 2, 5]
duplicates = find_duplicates(arr)
print(duplicates)  # output: [1, 2]
