"""
## Problem - Rotated Lists

We'll solve the following problem step-by-step:

 You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.

 Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 

"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
"""
"""
Here's the systematic strategy we'll apply for solving problems:

State the problem clearly. Identify the input & output formats.
Come up with some example inputs & outputs. Try to cover all edge cases.
Come up with a correct solution for the problem. State it in plain English.
Implement the solution and test it using example inputs. Fix bugs, if any.
Analyze the algorithm's complexity and identify inefficiencies, if any.
Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"""
# Linear search:
# ________________
"""
Our first goal should always be to come up with a correct solution to the problem, which may not necessarily be the most efficient solution. Try to think of a solution before you read further.

Coming up with the correct solution is quite easy, and it's based on this insight: If a list of sorted numbers is rotated k times, then the smallest number in the list ends up at position k (counting from 0). Further, it is the only number in the list which is smaller than the number before it. Thus, we simply need to check for each number in the list whether it is smaller than the number that comes before it (if there is a number before it). Then, our answer i.e. the number of rotations is simply the position of this number is . If we cannot find such a number, then the list wasn't rotated at all.

Example: In the list [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], the number 3 is the only number smaller than its predecessor. It occurs at the position 4 (counting from 0), hence the array was rotated 4 times.

We can use the linear search algorithm as a first attempt to solve this problem i.e. we can perform the check for every position one by one. But first, try describing the above solution in your own words, that make it clear to you.

Q (Optional): Describe the linear search solution explained above problem in your own words.

check for number smaller than the number before it.
it is smallest number in the list.
it's position counting from zero is the number of times the list is rotated.
return the position as output
"""
def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?
    
    while position < len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position - 1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return position                    # What if none of the positions passed the check 

# Binary search:
#-------------------
"""
 Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
As you might have guessed, we can apply Binary Search to solve this problem. The key question we need to answer in binary search is: Given the middle element, how to decide if it is the answer (smallest number), or whether the answer lies to the left or right of it.

If the middle element is smaller than its predecessor, then it is the answer. However, if it isn't, this check is not sufficient to determine whether the answer lies to the left or the right of it. Consider the following examples.

[7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)

[1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

Here's a check that will help us determine if the answer lies to the left or the right: If the middle element of the list is smaller than the last element of the range, then the answer lies to the left of it. Otherwise, the answer lies to the right.

Do you see why this strategy works?

7. Come up with a correct solution for the problem. State it in plain English.
Before we implement the solution, it's useful to describe it in a way that makes most sense to you. In a coding interview, you will almost certainly be asked to describe your approach before you start writing code.

Q (Optional): Describe the binary search solution explained above problem in your own words.

check the middle element. If it is smaller than the before number, then it is the answer. If not, continue to next steps.
if middle element is smaller than the last element of the list, then desired element is to the left.
else, to the right
keep checking until you find the middle element smaller than it's predecessor.
"""
def count_rotations_binary(nums):
    if not nums:
        return 0

    lo = 0
    hi = len(nums) - 1

    # If the array is already sorted, 0 rotations
    if nums[lo] <= nums[hi]:
        return 0

    while lo < hi:
        mid = (lo + hi) // 2

        # If nums[mid] > nums[hi], the rotation point (smallest element) is in the right half [mid+1...hi]
        if nums[mid] > nums[hi]:
            lo = mid + 1
        # If nums[mid] <= nums[hi], the rotation point (smallest element) is in the left half [lo...mid]
        # This includes the case where mid itself is the smallest element.
        else:
            hi = mid

    return lo
