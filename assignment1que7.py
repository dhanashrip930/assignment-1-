#Move all the negative elements to one side of the array

def move_negatives_to_one_side(arr):
    """
    Moves all the negative elements in the given array to one side.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] < 0 and arr[right] >= 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0:
            left += 1
        else:
            right -= 1
            
    return arr


# Example usage
arr = [1, -2, 3, -4, 5, -6]
print(move_negatives_to_one_side(arr))  