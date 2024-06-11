# Problem Set 1: Palindrome Pairs

## Problem Description
Given a list of unique words, your task is to find all pairs of distinct indices (i, j) in the list so that
the concatenation of the two words, i.e., words[i] + words[j], forms a palindrome.

## Solution Overview
- We need to find pairs of words that, when concatenated, form a palindrome.
- A palindrome is a string that reads the same backward as forward.
- If a string is a palindrome, then the reverse of its prefix or suffix must match another string in the list for the concatenation to form a palindrome.
- We can break down each word into prefixes and suffixes and check if these parts form palindromes. In the context of the problem, the terms "prefix" and "suffix" refer to segments of the word that are split at a specific index.
- Using PYTHON we can use a dictionary for fast look-ups. This allows us to quickly check if the reverse of a prefix or suffix exists in the list.
- For each word in the list, iterate through all possible split points to divide the word into a prefix and a suffix.
- Check if either the prefix or the suffix is a palindrome.
- If the prefix is a palindrome, check if the reverse of the suffix exists in the list.
- If the suffix is a palindrome, check if the reverse of the prefix exists in the list.
- Ensure that the indices of the words are distinct to avoid self-pairing since a word should not pair with itself.


## Instructions to Run the Code
Assuming that python is already installed in your local machine, downloading the *.py file and running it will do the work.

- *Running using CLI / Terminal*
    -   using a command line interface or a terminal (cmd, git bash, etc.) you can run the code using:
    -   example using absolute path:
            ```python <path_to_file>\palindrome_pairs.py```
    -   example when already in directory of python file:
            ```python palindrome_pairs.py```

- *Running using an IDE or VScode*
    -   an IDE have a run button in order to run the code which will also have their own terminal where output will be shown.
        Example IDE - PyCharm: https://www.jetbrains.com/pycharm/
   
    -   you can also use VScode to run your code: https://code.visualstudio.com/download