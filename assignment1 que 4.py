#In an array, Count Pairs with given sum
def count_pairs(arr, target_sum):
    """
    Returns the number of pairs in the given array that add up to the given target sum.
    """
    count = 0
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)
        
    return count

# Example usage
arr = [1, 2, 3, 4, 5]
target_sum = 6
print(count_pairs(arr, target_sum)) 