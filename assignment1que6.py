#Find the Kth largest and Kth smallest number in an array
def find_kth_largest_smallest(numbers, k):
    """
    Finds the kth largest and kth smallest numbers in the given list of integers.
    """
    # Sort the list in ascending order to find the kth smallest number
    smallest = sorted(numbers)[k-1]
    
    # Sort the list in descending order to find the kth largest number
    largest = sorted(numbers, reverse=True)[k-1]
    
    return smallest, largest

# Example usage
numbers = [3, 5, 2, 8, 1, 9, 4]
k = 3
smallest, largest = find_kth_largest_smallest(numbers, k)
print(f"{k}th smallest number: {smallest}") # Output: 3
print(f"{k}th largest number: {largest}") # Output: 5
