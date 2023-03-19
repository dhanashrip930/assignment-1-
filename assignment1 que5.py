#Find duplicates in an array

def find_duplicates(arr):
    """
    Returns a list of duplicates in the input array.
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage:
my_arr = [1, 2, 3, 2, 4, 3, 5, 6, 5]
duplicates = find_duplicates(my_arr)
print(duplicates) # Output: [2, 3, 5]