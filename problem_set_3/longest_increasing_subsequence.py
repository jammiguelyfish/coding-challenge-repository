def lengthOfLIS(nums):
    """
    Find the length of the longest increasing subsequence in the given array.
    
    Parameters:
    nums (List[int]): An unsorted array of integers
    
    Returns:
    int: Length of the longest increasing subsequence
    """
    # Check if the input list is empty
    if not nums:
        return 0

    # Initialize the dp array where each element is 1
    dp = [1] * len(nums)
    
    # Fill dp array with the length of the longest increasing subsequence ending at each index
    for i in range(1, len(nums)):
        for j in range(i):
            # If nums[i] is greater than nums[j], it can be appended to the increasing subsequence that ends at nums[j]
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The result is the maximum value in dp array
    return max(dp)

def main():
    """
    Demonstrate the longest increasing subsequence solution.
    """
    # Example usage
    inputNumbers = [10, 9, 2, 5, 3, 7, 101, 18]
    result = lengthOfLIS(inputNumbers)
    print(result)  # Output: 4

if __name__ == '__main__':
    main()
