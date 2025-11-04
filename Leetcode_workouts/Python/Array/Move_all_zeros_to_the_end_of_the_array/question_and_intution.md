## 283. Move Zeroes

- Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
- Input: nums = [0,1,0,3,12]
- Output: [1,3,12,0,0]

Example 2:
- Input: nums = [0]
- Output: [0]
 

Constraints:
- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

### Better Approach

#### Edge cases
- It is given that the array is not an empty array, so it not bother.
- If the array is full of non-zeros.
- If the array is full of zeros.. 

#### Basic flow:
- First run a loop to find the index of the first zero. Use a variable to track of the first zero in the array.
- Check if the first zero variable is not positive, then array contains no zeros, return array.
- Run a loop from next index after first zero index. Check the current index value is non zero. If non zero then swap it with the firs zero index.
-  At this moment, the first zero index contains the non zero value and the current index contains the zero. So move the first zero index to next index.
- After the loops end, all the zeros will be at the end.

#### Complexity:
- Time complexity = O(k) + O(n - k) = O(k)               where O(k) for finding first zero and O(n - k) is for the loop to swap elements.
- Space complexity = o(1) 