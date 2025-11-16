class Solution:
    def two_sum(nums:list, sum:int):
        n = len(nums)
        find = {}
        for i in range(n):
            more = sum - nums[i]
            if more in find.keys():
                return [find[more], i]
            find[nums[i]] = i

        return [-1, -1]