"""
#1. Binary Search Template 1 (MOST BASIC)
Used to search for an element or condition which can be determined by accessing a SINGLE index in the array

No post-processing required because at each step, you are checking to see if the element has been found.
If you reach the end, then you know the element is not found


Key Conditions:

Initial Condition: left = 0, right = length-1
Termination: left > right

Searching Left: right = mid - 1
Searching Right: left = mid + 1

"""


def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    
    #***LESS THAN OR EQUAL
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
