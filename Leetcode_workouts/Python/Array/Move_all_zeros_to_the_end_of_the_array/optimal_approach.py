class Solution:
    def move_zeros_to_last(self, nums):
        n = len(nums)
        first_zero = -1
        for i in range(n):
            if nums[i] == 0:
                first_zero = i
                break
        
        if first_zero == -1:
            return nums
        
        for curr in range(first_zero+1, n):
            if nums[curr] != 0:
                nums[first_zero], nums[curr] = nums[curr], nums[first_zero]
                first_zero += 1

        return nums
