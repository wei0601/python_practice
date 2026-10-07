def three_sum(nums):
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    :param nums: List[int] - List of integers
    :return: List[List[int]] - List of unique triplets that sum to zero
    """
    nums.sort()
    result = []
    