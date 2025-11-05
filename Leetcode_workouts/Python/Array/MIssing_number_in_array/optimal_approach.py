# solution one
class Solution1:
    def missing_number(self, nums):
        n = len(nums)

        n_sum = (n * (n + 1)/2)
        nums_sum = 0
        for i in range(n):
            nums_sum += nums[i]
        return nums_sum - n_sum
    
# solution two
class Solution2:
    def missing_number(self, nums):
        n = len(nums)
        XOR1, XOR2 = 0, 0

        for i in range(n):
            XOR1 += XOR1 ^ nums[i]
            XOR2 += XOR2 ^ i
        XOR2 += XOR2 ^ n
    
        return XOR2 ^ XOR1
