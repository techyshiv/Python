def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Find the length of the longest substring with at most k distinct characters.
    
    Args:
        s (str): The input string.
        k (int): The maximum number of distinct characters allowed in the substring.
        
    Returns:
        int: The length of the longest substring with at most k distinct characters.
    
    Examples:
        >>> longest_substring_with_k_distinct("eceba", 2)
        3
        
        >>> longest_substring_with_k_distinct("aa", 1)
        2
        
        >>> longest_substring_with_k_distinct("abcabcabc", 2)
        2
        
        >>> longest_substring_with_k_distinct("aabbcc", 3)
        6
    """
    # Edge case: If k is 0, no valid substring can exist
    if k == 0:
        return 0
    
    # Hashmap to store the frequency of characters in the current window
    char_count = {}
    
    left = 0  # Left pointer of the sliding window
    max_len = 0  # Maximum length of the substring with at most k distinct characters
    
    # Iterate over the string using the right pointer
    for right in range(len(s)):
        # Add the current character to the hashmap or increase its count
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # If the window has more than k distinct characters, shrink it from the left
        while len(char_count) > k:
            char_count[s[left]] -= 1  # Reduce the count of the leftmost character
            if char_count[s[left]] == 0:
                del char_count[s[left]]  # Remove the character from the map if its count is zero
            left += 1  # Move the left pointer to shrink the window
        
        # Update the maximum length of the valid window
        max_len = max(max_len, right - left + 1)
    
    return max_len


if __name__ == "__main__":
    import doctest
    doctest.testmod()
