## Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



### Better Approach

#### Basic flow:
- We can imagine the array as two separate section. 
- If the array is [1, 2, 3, 4, 5, 6, 7] and k = 3. 
- First array = [1, 2, 3, 4] and second array = [5, 6, 7]
- Store the second imaginary array in a new array. So new array = [ 5, 6, 7]
- Later move the first imaginary array to the extreme right of the array. So after doing, the array would be like this [1, 2, 3, 1, 2, 3, 4]
- Now replace the first 3 index (value of k = 3) with the new array created.
- It would be like [5, 6, 7, 1, 2, 3, 4]

#### Complexity:
- Time complexity =  O(d) + O(n - d) + o (d) = o(n)
- space complexity = O(d)


### Optimal Approach

#### Basic flow:
- If the array = [1, 2, 3, 4, 5, 6, 7] and k = 3, rotated array = [5, 6, 7, 1, 2, 3, 4].
- Consider two imaginary arrays as in the better approach. 
- Reverse the first imaginary array gives [4, 3, 2, 1].
- Reverse the second imaginary array gives [7, 6, 5].
- So the combined array will be like [4, 3, 2, 1, 7, 6, 5].
- Later reverse the entire array gives the result [5, 6, 7, 1, 2, 3, 4].
- Basically, these are in-place reversing using a built in reverse function or custom made function.

#### Complexity:
- Time complexity = O(d) + O(n - d) + O(n) = O(n)
- Space complexity = o(1)



### Edge Cases:
- Empty array.
- Only One element in array.
- If the length of the array is n and there is a possibility that the array sorted more than n times. So n times rotated means logically 0 times rotated. So find actually times of rotation using d = d%n.