class Solution:
    def longest_sub_array(self, nums, k):
        n = len(nums)
        left, right = 0, 0
        sum = nums[0]
        maxlen = 0

        while (right < n):

            while (left <= right) and (sum > k):
                sum -= nums[left]
                left += 1

            if sum == k:
                maxlen = max(maxlen, (right - left) + 1)

            right += 1
            sum += nums[right]
            

        return maxlen

            
            
            

