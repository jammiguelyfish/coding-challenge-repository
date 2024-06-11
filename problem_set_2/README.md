# Problem Set 2: Valid Parentheses

## Problem Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Solution Overview
- In this problem, a stack data structure is well-suited. A stack is a Last-In-First-Out (LIFO). This allows us to keep track of the most recent opening bracket and ensure it gets properly closed.
- Initialize an empty stack.
- Iterate through each character in the input string.
- If the character is an opening bracket ('(', '{', '['), push it onto the stack.
- If the character is a closing bracket (')', '}', ']'):
- Check if the stack is empty (indicating an unmatched closing bracket).
- Pop the top element from the stack and check if it matches the corresponding opening bracket.
- If it does not match, the string is invalid.
- After processing all characters, if the stack is empty, all brackets were matched correctly; otherwise, there are unmatched opening brackets.

## Instructions to Run the Code
Assuming that python is already installed in your local machine, downloading the *.py file and running it will do the work.

- *Running using CLI / Terminal*
    -   using a command line interface or a terminal (cmd, git bash, etc.) you can run the code using:
    -   example using absolute path:
            ```python <path_to_file>\valid_parentheses.py```
    -   example when already in directory of python file:
            ```python valid_parentheses.py```

- *Running using an IDE or VScode*
    -   an IDE have a run button in order to run the code which will also have their own terminal where output will be shown.
        Example IDE - PyCharm: https://www.jetbrains.com/pycharm/
   
    -   you can also use VScode to run your code: https://code.visualstudio.com/download