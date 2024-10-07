def three_sum(arr: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array that sum up to zero.
    
    Args:
        arr (list[int]): The input array of integers.
        
    Returns:
        list[list[int]]: A list of lists, where each inner list contains 3 integers that sum to zero.

    Examples:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        
        >>> three_sum([0, 0, 0])
        [[0, 0, 0]]
        
        >>> three_sum([-2, 0, 1, 1, 2])
        [[-2, 0, 2], [-2, 1, 1]]
        
        >>> three_sum([1, 2, -2, -1])
        []
        
        >>> three_sum([3, 0, -2, -1, 1, 2])
        [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    """
    arr.sort()  
    result = []
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == 0:
                result.append([arr[i], arr[left], arr[right]])
                
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1  
            else:
                right -= 1  
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
