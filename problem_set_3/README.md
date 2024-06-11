# Problem Set 3: Longest Increasing Subsequence

## Problem Description
**For context**. The "Longest Increasing Subsequence" is a common problem in computer science and
dynamic programming. In the context of an array of integers, the goal is to find the length of the longest
subsequence of a given array such that all elements of the subsequence are sorted in increasing order.

**Here's a more detailed explanation**:
- **Subsequence**: A subsequence is a sequence of elements that appear in the same order as they
are in the original sequence, but not necessarily consecutively.
- **Increasing Subsequence**: An increasing subsequence is a subsequence in which the elements are
in strictly increasing order.

The "Longest Increasing Subsequence" problem asks for the length of the longest increasing
subsequence in a given array. For example, given the array: [10, 9, 2, 5, 3, 7, 101, 18]

One possible increasing subsequence is [2, 5, 7, 18], and the length of this subsequence

Solving this problem efficiently often involves dynamic programming techniques, where you build up a
solution for each subproblem and use those solutions to solve the overall problem.

## Solution Overview
- Create a dp array of the same length as the input array, initializing all elements to 1 because the minimum length of any increasing subsequence is 1 (the element itself).
- For each element nums[i], iterate through all previous elements nums[j] where j < i.
- If nums[i] is greater than nums[j], update dp[i] to be the maximum of its current value and dp[j] + 1.
- The length of the longest increasing subsequence will be the maximum value in the dp array.

## Instructions to Run the Code
Assuming that python is already installed in your local machine, downloading the *.py file and running it will do the work.

- *Running using CLI / Terminal*
    -   using a command line interface or a terminal (cmd, git bash, etc.) you can run the code using:
    -   example using absolute path:
            ```python <path_to_file>\longest_increasing_subsequence.py```
    -   example when already in directory of python file:
            ```python longest_increasing_subsequence.py```

- *Running using an IDE or VScode*
    -   an IDE have a run button in order to run the code which will also have their own terminal where output will be shown.
        Example IDE - PyCharm: https://www.jetbrains.com/pycharm/
   
    -   you can also use VScode to run your code: https://code.visualstudio.com/download