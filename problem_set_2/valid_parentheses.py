def isValid(s):
    """
    Check if the input string of brackets is valid.
    
    Args:
    s (str): Input string containing only '(', ')', '{', '}', '[' and ']'.
    
    Returns:
    bool: True if the string is valid, False otherwise.
    """
    # Map of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to track opening brackets
    stack = []

    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:
            # Pop the top element from the stack or use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check for matching opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # Push opening bracket onto the stack
            stack.append(char)

    # Valid if stack is empty at the end
    return not stack

def main():
    """
    Demonstrate the valid parentheses solution.
    """
    # Example usage
    inputString = "()[]{}"
    result = isValid(inputString)
    print(result)  # Output: True
    
    # Test Cases
    """
    print(isValid("()[]{}"))  # True
    print(isValid("([)]"))    # False
    print(isValid("{[]}"))    # True
    print(isValid("{[()]"))   # False
    print(isValid("{[()]}"))  # True
    print(isValid("([{}])"))  # True
    print(isValid("[({})](]"))# False
    """
    

if __name__ == '__main__':
    main()
