class solution:
    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    def rotate(self, nums, d):
        n = len(nums)
        d = d % n

        if n < 2:
            return nums
        
        self.reverse(nums, 0, (n - d - 1))
        self.reverse(nums, (n - d), (n - 1))
        self.reverse(nums, 0, (n  - 1))
        
        return nums