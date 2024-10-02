"""
Find Sum of minimum and maximum elements of all subarrays of given size K
Reference of Problem: https://www.geeksforgeeks.org/sliding-window-problems-identify-solve-and-interview-questions/
Reference of Sliding Window : https://medium.com/@ayushisharma5141/sliding-window-approach-types-and-problems-b1e256e2e92b


Python doctest can be run with the following command:
python -m doctest -v equilibrium_index_in_array.py

Given an array of both positive and negative integers, 
the task is to compute sum of minimum and maximum elements of all sub-array of size k.

Examples: 
    Input : arr[] = {2, 5, -1, 7, -3, -1, -2}   
    K = 4 <window-size>
    Output : 18
"""

def sum_of_k_subarray(arr: list[int], window_size: int) -> int:
    """
    Find sum of max and min elements of all sub-arrays of size k

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int: The sum of max and min elemnets of all sub-arrays of size k.

    Examples:
        >>> sum_of_k_subarray([2, 5, -1, 7, -3, -1, -2],4)
        18
        >>> sum_of_k_subarray([1, 3, 2, 4, 5], 2)
        24
        >>> sum_of_k_subarray([1, 3, -2, 8, -7, 10], 3)
        11
        >>> sum_of_k_subarray([-5, -1, -3, -4, -2], 3)
        -17
        >>> sum_of_k_subarray([10, 20, 30, 40], 1)
        200
    """
    start,end = 0,0
    sum = 0
    while (end < len(arr)):
        if (end-start+1 == window_size):
            max_elm = max(arr[start:end+1])
            min_elm = min(arr[start:end+1])
            sum += max_elm + min_elm
            start += 1
            end += 1
        elif (end-start+1 < window_size):
            end += 1
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
