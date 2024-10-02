"""
Find Sum of minimum and maximum elements of all subarrays of given size K
Reference of Problem: https://www.geeksforgeeks.org/sliding-window-problems-identify-solve-and-interview-questions/
Reference of Sliding Window : https://medium.com/@ayushisharma5141/sliding-window-approach-types-and-problems-b1e256e2e92b


Python doctest can be run with the following command:
python -m doctest -v sliding_window.py

Given an array of both positive and negative integers, 
the task is to compute sum of minimum and maximum elements of all sub-array of size k.

Examples: 
    Input : arr[] = {2, 5, -1, 7, -3, -1, -2}   
    K = 4 <window-size>
    Output : 18
"""

from collections import deque

def sum_of_k_subarray(arr: list[int], window_size: int) -> int:
    """
    Find the sum of the max and min elements of all sub-arrays of size k.

    Args:
        arr (list[int]): The input array of integers.
        window_size (int): Size of the sub-arrays.

    Returns:
        int: The sum of max and min elements of all sub-arrays of size k.

    Examples:
        >>> sum_of_k_subarray([2, 5, -1, 7, -3, -1, -2], 4)
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
    # Deques to store indices of the elements of interest
    max_deque = deque()
    min_deque = deque()
    total_sum = 0

    for i in range(len(arr)):
        if max_deque and max_deque[0] < i - window_size + 1:
            max_deque.popleft()
        if min_deque and min_deque[0] < i - window_size + 1:
            min_deque.popleft()

        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()
            
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()

        max_deque.append(i)
        min_deque.append(i)

        if i >= window_size - 1:
            max_element = arr[max_deque[0]]
            min_element = arr[min_deque[0]]
            total_sum += max_element + min_element

    return total_sum



if __name__ == "__main__":
    import doctest

    doctest.testmod()
