from typing import List


def majorityElement(self, nums: List[int]) -> int:
    """ function  to find the majority element in an array"""
    count = 1
    majEl = nums[0]
    if isValid(nums, len(nums)):
        for i in range(1, len(nums)):
            if nums[i] != majEl:
                count -= 1
                if count == 0:
                    majEl = nums[i]
                    count += 1
            else:
                count += 1
        count = 0
        for i in nums:
            if i == majEl:
                count += 1
        if count > len(nums) // 2:
            return majEl
        else:
            return None


def isValid(array, n):
    if n != array.length:
        return False
    elif n < 1 or n > 5 * (10 ** 4):
        return False
    elif isInValidArrayEl(array):
        return False
    else:
        return True


def isInValidArrayEl(array):
    return any(num > 10 ** 9 or num < -10 ** 9 for num in array)


