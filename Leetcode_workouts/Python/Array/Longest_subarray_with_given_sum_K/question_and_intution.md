## Longest Sub Array with given sum K

- Given an array and a sum k, we need to print the length of the longest subarray that sums to k.



Example 1:
- Input: nums = [2,3,5,1,9], k = 10
- Output: 3

Example 2:
- Input: nums = [2] k = 2
- Output: 2
 

Constraints:
- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

### Optimal Approach

#### Edge cases
- It is given that the array is not an empty array, so it not bother.
- Only one element in the array.
- Multiple sub arrays.
- 

#### Basic flow:
- Implement a two pointer approach. Left and right pointers.
- Both pointers starts from 0th index.
- The left pointer stay at 0th index, the right index increment and do summation. 
- After each iteration, three possible answers available.
- Sum is less than k, so the right keep incrementing and do summation of right index value to the sum.
- Sum is equal to k, so assign the sub array length into a variable called max length, by the formula (right - left) + 1.
- Sum is greater than k, subtract the left index element from sum. There is a possibility that still the sum is greater than k. So, do this operation in a while loop until the sum is less than k. Also increment the left pointer.


#### Complexity:
- Time complexity = O(n)              
- Space complexity = o(1) 