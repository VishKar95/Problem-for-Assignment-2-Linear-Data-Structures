def count_pairs_with_sum(arr, target_sum):
    freq = {}
    count = 0
    
    # count frequency of each element in the array
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    
    # count pairs with given sum
    for x in arr:
        diff = target_sum - x
        if diff in freq:
            count += freq[diff]
            if x == diff:
                count -= 1
    
    return count // 2
arr = [1, 5, 7, -1, 5]
target_sum = 6
count = count_pairs_with_sum(arr, target_sum)
print(count)  # output: 3
