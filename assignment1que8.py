#Reverse a string using a stack data structure

def reverse_string(s):
    """
    Returns the input string in reversed order.
    """
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return reversed_s

# Example usage:
my_string = "Hello, world!"
reversed_string = reverse_string(my_string)
print(reversed_string) # Output: "!dlrow ,olleH"