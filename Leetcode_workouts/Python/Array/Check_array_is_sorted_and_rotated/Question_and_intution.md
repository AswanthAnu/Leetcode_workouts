## 1752. Check if Array Is Sorted and Rotated

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.



#### Example 1:
- Input: nums = [3,4,5,1,2]
- Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

#### Example 2:
- Input: nums = [2,1,3,4]
- Output: false
Explanation: There is no sorted array once rotated that can make nums.

#### Example 3:
- Input: nums = [1,2,3]
- Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

#### Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

### Better Approach

#### Edge cases
- It is given that the array is not an empty array, so it not bother.
- An array of size 1 is simply sorted and rotated. So no special case need to be added in the code.
- Make sure to check the last element and first element, at that point it might goes as unsorted.

#### Basic flow:
- Solve using a variable named count.
- Just check if the current element is greater that the next element, If yes, then increase the count by 1.
- An ascending sorted and rotated array only have one point were the current element is greater than the next element.
- If count is greater than 1, then its unsorted. Return False. 
- There is a loop hole. Example if the array is [4, 1, 2, 3, 6]. In this case the count only gives 1 after executing the full code and return True as sorted. But it is unsorted. 
- If we only check [current element, next element]. The index goes like [0, 1], [1, 2] , [2, 3]. 
- So we also need to check the last element and the first element at last. So the index should goes like [0, 1], [1, 2], [2, 3] and [3, 0].
- For that, the next element index is generated using [(i + 1) % length of the array].

#### Complexity:
- Time complexity = O(n)
- Space complexity = o(1)