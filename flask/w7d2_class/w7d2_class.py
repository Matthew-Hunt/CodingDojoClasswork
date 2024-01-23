# Given a list of intergers move all the zeros to the end of the list
# Example: [ 0, 2, 1, 6, 4, 3, 6, 0, 3 ] would return [ 2, 1, 6, 4, 3, 6, 3, 0, 0 ]

nums = [0, 2, 1, 6, 4, 3, 6, 0, 3]

def move_zeroes_to_end(nums):
    last_non_zero_index =  0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
            last_non_zero_index += 1
    return nums


print(move_zeroes_to_end(nums))



