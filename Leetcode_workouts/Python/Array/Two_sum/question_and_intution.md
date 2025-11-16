## Two Sum 1
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:
- Input: nums = [2,7,11,15], target = 9
- Output: [0,1]
- Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
- Input: nums = [3,2,4], target = 6
- Output: [1,2]

Example 3:
- Input: nums = [3,3], target = 6
- Output: [0,1]
 
Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

### Optimal Approach

#### Edge cases
- Minimum two elements in the list, so not an issue.
- All the elements are zero.
- Sum is zero.


#### Basic flow:
- Hashing is the solution.
- Create an empty dictionary called find### Better Approach

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
- Space complexity = o(1) . In the dictionary the key is the current_element which is used as the remaining value to get the sum and value is the index.
- Loop through the list, Calculate the remaining value need to get the sum. For that use the mathematical formula. More = Sum - current_element.
- Check if the More is in the keys list of dictionary ? If yes, then return the value associated with the key along with the current index (return find([nums[i], i]).
- If more is not in the dictionary, then add the current_value as the key and the index as the value in dictionary.
- Else return([-1, -1]), not values to make the sum.

#### Complexity:
- Time complexity = O(n) + O(log n)          where O(n) for finding looping and O(log n) is for finding the key in dict.
- Space complexity = o(n) 