## 268. Missing Number

- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

- Input: nums = [3,0,1]
- Output: 2
- Explanation:
 n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
- Input: nums = [0,1]
- Output: 2
- Explanation:
 n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
- Input: nums = [9,6,4,2,3,5,7,0,1]
- Output: 8
- Explanation:
 n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

- n == nums.length
- 1 <= n <= 104
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

### Better Approach

#### Edge cases
- It is given that the array is not an empty array, so it not bother.
- Starts from 0 to n.
- Only one element.

#### Basic flow:
- This problem have two optimal solutions
- First one: 
    - Using sum of n natural number formula.
    - As the elements in the array is starts from 0 to n, with continuous values.
    - Use two variables, one to calculate the sum of n natural numbers [n * (n + 1)/2].
    - Second variable used to calculate the sum of elements in the array using a for loop.
    - As the array miss one element, the difference in the n natural number sum and sum of elements in the array gives the missing element.
- Second one:
    - Using XOR. XOR of two same elements gives 0.
    - So using a loop find the XOR of elements in the array. That will give a value.
    - In the same loop, find the XOR of elements from 0 to n. That will give another value.
    - XOR first and second value gives the difference

#### Complexity:
- Time complexity = O(n)          
- Space complexity = o(1) 