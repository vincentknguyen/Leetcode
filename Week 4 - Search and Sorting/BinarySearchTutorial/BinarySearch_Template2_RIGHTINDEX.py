"""
Template 2


Used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.

Search Condition needs to access element's immediate right neighbor (ex: if you need to check two elements in sequence, current and next to the right)

Use element's right neighbor to determine if condition is met and decide whether to go left or right

Gurantees Search Space is at least 2 in size at each step

Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.


Key Conditions

Initial Condition: left = 0, right = length
Termination: left == right
Searching Left: right = mid
Searching Right: left = mid + 1

"""


def binarySearch(nums, target):
    if len(nums) == 0:
        return -1
    
    #CONDITION, as opposied to right = len(nums) - 1
    
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            
            #Searching on the RIGHT
            left = mid + 1
        else:
            
            #CONDITION, as opposed to right = mid - 1
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1



