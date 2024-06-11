def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    
    Args:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def palindrome_pairs(words):
    """
    Find all unique pairs of indices (i, j) such that the concatenation
    of words[i] and words[j] forms a palindrome.
    
    Args:
    words (list of str): The list of unique words.
    
    Returns:
    list of list of int: A list of pairs of indices where each pair 
                         [i, j] forms a palindrome when concatenating 
                         words[i] and words[j].
    """
    pairs = []
    word_index = {word: i for i, word in enumerate(words)}

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            # Check if the prefix is a palindrome and the reverse of the suffix exists in the words
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_index and word_index[reversed_suffix] != i:
                    pairs.append([word_index[reversed_suffix], i])
            
            # Check if the suffix is a palindrome and the reverse of the prefix exists in the words
            # Avoid duplicate pairs by ensuring j != len(word)
            if j != len(word) and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_index and word_index[reversed_prefix] != i:
                    pairs.append([i, word_index[reversed_prefix]])
    
    return pairs

def main():
    """
    Main function to demonstrate the usage of the palindrome_pairs function.
    """
    # Example usage
    input_words = ["bat", "tab", "cat"]
    result = palindrome_pairs(input_words)
    print(result)  # Output: [[1, 0], [0, 1]]

if __name__ == '__main__':
    main()
