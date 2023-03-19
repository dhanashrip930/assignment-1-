#Evaluate a postfix expression using stack
def evaluate_postfix(expression):
    """
    Evaluates the given postfix expression and returns the result.
    """
    stack = []
    
    for char in expression:
        # If the character is a digit, push it onto the stack
        if char.isdigit():
            stack.append(int(char))
        # If the character is an operator, pop the top two elements from the stack
        # and apply the operator to them, then push the result back onto the stack
        elif char in "+-*/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2
                
            stack.append(result)
            
    # The final element on the stack is the result of the expression
    return stack.pop()

# Example usage
expression = "23+4*"
print(evaluate_postfix(expression))
