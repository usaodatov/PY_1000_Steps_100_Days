'''
QUESTION #26

You are given a string, and you need to count the number of vowels and consonants in the string.

Input Format:
1. The input contains a single line: the string.

Constraints:
- 1 ≤ len(string) ≤ 10^3
- The string consists of alphabetic characters only.

Output Format:
Print two integers: the number of vowels and consonants in the string.

Example Input:
hello

Example Output:
2 3

Clues to Solve:
1. Use a set to store vowels for easy lookup.
2. Loop through the string to count vowels and consonants.
3. Ignore case differences by converting the string to lowercase.

How it works:
1. **Input Reading**:
   - Read the string as input.
2. **Initialize Counters**:.
   - Use variables to count vowels and consonants.
3. **Iterate Through the String**:
   - Check each character against the set of vowels.
   - Increment the respective counter.
4. **Output**:
   - Print the counts of vowels and consonants.
'''
from unittest.util import sorted_list_difference

# in_string = input('Please enter a word:  ').lower() # Read the string and convert it to lowercase.
#
# def count_vowels_consonants(in_string):
#     vowels = set('aeiou') # Set of vowels for reference and look up
#     vowel_count = 0
#     consonant_count = 0
#
#     for char in in_string:
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
#
#     return vowel_count, consonant_count
#
#
# print(count_vowels_consonants(in_string)) # Print the counts of vowels and consonants.
#
#
#
#
'''
QUESTION #27

You are given a list of integers and a target sum. You need to find all unique quadruplets (groups of four numbers) from the list that add up to the target sum.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers, the elements of the list.
3. The third line contains an integer, the target sum.

Constraints:
- 4 ≤ n ≤ 200
- -10^3 ≤ integer ≤ 10^3
- -10^6 ≤ target sum ≤ 10^6

Output Format:
Print all unique quadruplets (in any order) that add up to the target sum. Each quadruplet should be space-separated and printed on a new line.

Example Input:
6
1 0 -1 0 -2 2
0

Example Output:
-2 -1 1 2
-2 0 0 2
-1 0 0 1

Clues to Solve:
1. **Sorting**:
   - Sort the input list to make it easier to skip duplicates and use multiple pointers.
2. **Two-pointer Approach**:
   - Use two pointers for the innermost loop to find pairs that complement the other two numbers.
3. **Deduplication**:
   - Avoid adding duplicate quadruplets by skipping repeated values.

How it works:
1. **Input Reading**:
   - Parse the size of the list (`n`), the list of integers, and the target sum.

2. **Sort the List**:
   - Sorting helps to systematically explore combinations and skip duplicates efficiently.

3. **Iterative Approach**:
   - Fix the first two numbers using nested loops, then use a two-pointer approach to find pairs that complete the quadruplet.

4. **Output**:
   - Print each unique quadruplet on a new line.
'''

# the_list = list(map(int, input('the list  :  ').split()))
# the_value = int(input('the value  :  '))
#
# def three_sum(nums, target):
#     nums.sort()  # Sort the list to make it easier to find triplets
# #     result = []
# #
# #     for i in range(len(nums) - 3): # Fix the first number
# #         if i > 0 and nums[i] == nums[i - 1]: #  Skip duplicates
# #             continue # Skip duplicates / loop back to the next iteration
# #
# #         for j in range(i + 1, len(nums) - 2): # Fix the second number
# #             if j > i + 1 and nums[j] == nums[j - 1]: #
# #                 continue
# #
# #             left = j + 1 # Use two pointers to find the other two numbers
# #             right = len(nums) - 1
# #
# #             while left < right:#  Find the other two numbers
# #                 total = nums[i] + nums[j] + nums[left] + nums[right]
# #
# #                 if total == target: # Check if the sum is equal to the target
# #                     result.append([nums[i], nums[j], nums[left], nums[right]])
# #                     left += 1
# #                     right -= 1
# #
# #                     while left < right and nums[left] == nums[left - 1]:# Skip duplicates
# #                         left += 1
# #
# #                     while left < right and nums[right] == nums[right + 1]: #
# #                         right -= 1
# #
# #                 elif total < target: # Move the pointers
# #                     left += 1
# #                 else:
# #                     right -= 1
# #
# #     return result
# #
# # print(three_sum(the_list, the_value))



# the_list = list(map(int, input('the list  :  ').split()))
# the_value = int(input('the value  :  '))

'''
QUESTION #28

You are given a list of integers, and you need to find all unique triplets in the list that add up to a target sum. However, instead of a fixed target, your program should calculate and return all unique triplets that add up to 0.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers, the elements of the list.

Constraints:
- 3 ≤ n ≤ 10^4
- -10^5 ≤ integer ≤ 10^5

Output Format:
Print all unique triplets that sum up to 0. Each triplet should be printed on a new line, sorted in ascending order.

Example Input:
6
-1 0 1 2 -1 -4

Example Output:
-1 -1 2
-1 0 1

Clues to Solve:
1. **Sorting for Efficiency**:
   - Sort the list to simplify finding and deduplicating triplets.
2. **Two-Pointer Technique**:
   - Fix the first number and use two pointers to find the other two numbers.
3. **Avoid Duplicates**:
   - Skip duplicate values to ensure only unique triplets are included.

How it works:
1. **Input Reading**:
   - Parse the size of the list (n) and the integers in the list.
2. **Sort the List**:
   - Sorting simplifies deduplication and allows for efficient two-pointer traversal.
3. **Iterate Through the List**:
   - For each number, fix it as the first element of the triplet.
4. **Find Pairs**:
   - Use two pointers (`left` and `right`) to find pairs of numbers that sum up to `-nums[i]`.
5. **Avoid Duplicates**:
   - Skip duplicate numbers during iteration and while moving the pointers.
6. **Output Results**:
   - Print each unique triplet on a new line.
'''

#
# the_list = list(map(int, input('the list  :  ').split()))
#
# def three_uniques(nums):
#     nums.sort()  # Sort the list to simplify deduplication and pointer logic
#     result = []
#
#     for i in range(len(nums) - 2):  # Fix the first number
#         if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
#             continue  # Skip to the next iteration
#
#         left, right = i + 1, len(nums) - 1  # Two-pointer setup
#         while left < right:
#             total = nums[i] + nums[left] + nums[right] #
#
#             if total == 0:  # Found a triplet
#                 result.append((nums[i], nums[left], nums[right])) # Append the triplet
#                 left += 1
#                 right -= 1
#
#                 # Skip duplicates for the second and third numbers
#                 while left < right and nums[left] == nums[left - 1]: # Skip duplicates / loop back to the next iteration
#                     left += 1
#                 while left < right and nums[right] == nums[right + 1]: # skip duplicates / loop back to the next iteration
#                     right -= 1
#
#             elif total < 0:  # Sum is too small, move left pointer right
#                 left += 1
#             else:  # Sum is too large, move right pointer left
#                 right -= 1
#
#     return result
#
# print(three_uniques(the_list))


'''
QUESTION #30

You are given a string, and you need to find all unique permutations of its characters.

Input Format:
The first line contains a string s.

Constraints:
- 1 <= len(s) <= 10
- The string contains only lowercase alphabetic characters.

Output Format:
Print all unique permutations of the string, one per line, in lexicographical order.

Example Input:
abc

Example Output:
abc
acb
bac
bca
cab
cba

Clues to Solve:
1. **Understand Permutations**:
   - Permutations are all possible arrangements of a string's characters.
   - Ensure there are no duplicates in the output.

2. **Approaches**:
   - Use recursion to generate permutations by fixing one character at a time.
   - Use Python's `itertools.permutations` to simplify the process.
   - Sort the results to ensure lexicographical order.

3. **Output Requirements**:
   - Ensure uniqueness by using a set or sorting after generation.
   - Print each permutation on a new line.

How it works:
1. **Input Reading**:
   - Read the string as input.

2. **Generate Permutations**:
   - Use recursion or a library to generate all possible permutations.

3. **Filter and Sort**:
   - Remove duplicates (if any) and sort the permutations lexicographically.

4. **Output**:
   - Print each permutation on a new line.
'''

# import itertools # Import the itertools module to generate permutations of the string.
#
# the_string = input('Please enter a word for permutations:  ')
#
# def unique_permutations(the_string):
#     permutations = itertools.permutations(the_string) # Generate all permutations
#     unique_permutations = set(permutations) # Remove duplicates
#     sorted_permutations = sorted(unique_permutations) # Sort the permutations
#     for perm in sorted_permutations:
#         print(''.join(perm))
#
# unique_permutations(the_string) # Print each unique permutation on a new line.
#
#
#









'''
QUESTION #30

You are given a list of integers and an integer k. Your task is to find the k-th smallest element in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers, the elements of the list.
3. The third line contains an integer k.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3
- 1 <= k <= n

Output Format:
Print the k-th smallest element in the list.

Example Input:
6
7 10 4 3 20 15
3

Example Output:
7

Clues to Solve:
1. **Sorting**:
   - Sort the list in ascending order.
   - The k-th smallest element is the element at index `k-1` in the sorted list.

2. **Optimized Approach**:
   - Use a heap (e.g., Python's `heapq`) to find the k-th smallest element without fully sorting the list.

3. **Handling Edge Cases**:
   - Ensure k is within the range `[1, n]`.
   - Handle cases where the list contains duplicate values.

How it works:
1. **Input Reading**:
   - Read the size of the list (`n`), the integers in the list, and the value of `k`.

2. **Sorting**:
   - Sort the list in ascending order.

3. **Retrieve k-th Element**:
   - Access the k-th smallest element using `sorted_list[k-1]`.

4. **Output**:
   - Print the k-th smallest element.
'''


the_list = list(map(int, input('the list  :  ').split()))
k= int(input('the value of k  :  '))


def kth_smallest_element(in_list, k):
   sorted_list = sorted(in_list) # Sort the list in ascending order /Sorting takes O(nlogn) time/ok for sml lists
   return sorted_list[k-1] # Return the k-th smallest element

print(kth_smallest_element(the_list, k)) # Print the k-th smallest element in the list.


#alternative solution
import heapq  # Import the heapq module for efficient heap operations

the_list = list(map(int, input('the list (alternative)  :  ').split()))
k = int(input('the value of k  :  '))


def kth_smallest_with_heap(in_list, k):
    """
    Finds the k-th smallest element using a min-heap.
    """
    heapq.heapify(in_list)  # Convert the list into a min-heap (O(n) operation)
    smallest = None

    for _ in range(k):  # Extract the smallest element k times
        smallest = heapq.heappop(in_list)  # Pop the smallest element from the heap

    return smallest  # The k-th pop gives the k-th smallest element


print(kth_smallest_with_heap(the_list, k))  # Print the k-th smallest element
