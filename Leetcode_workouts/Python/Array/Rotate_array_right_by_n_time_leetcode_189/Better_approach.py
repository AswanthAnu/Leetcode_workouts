class Solution:
    def rotate(self, nums, d):
        n = len(nums)
        d = d % n
        new = []

        if n < 2:
            return nums

        for i in range(0, d):
            new.append(nums[n - d + i])

        for j in range(1, n - d + 1):
            nums[n - j] = nums[n - d - j]
        
        for k in range(0, d):
            nums[k] = new[k]

        return nums
            
