"""
QUESTION #16
You are given a string, and you need to count the frequency of each character in the string.

Input Format:
- A single string containing alphabetic characters (both uppercase and lowercase).

Constraints:
- 1 <= len(string) <= 10^3

Output Format:
Print each character followed by its frequency in the order they appear.

Example Input:
aabbcc

Example Output:
a2b2c2

Clues to Solve:
- Use a dictionary to keep track of each character and its frequency.
- Iterate through the string to update the dictionary with counts.
- Use a loop to construct the output by iterating over the dictionary in the order of appearance.
"""


#
# the_string_in = input(' the string please: ')
#
# the_string = the_string_in[0::1]
#
#
# def num_of_occur(in_string):
#
#
#     keys = set() #unique elements
#
#     the_dict = {}
#
#     final_string = ''
#
#     for i in in_string:
#         keys.add(i)
#
#     for i in keys:
#         count_i = in_string.count(i)
#         the_dict.update({i : count_i})
#
#
#     for key,value in the_dict.items():
#         final_string += f'{key}{value}'
#
#     print(final_string)
#
#
#
# num_of_occur(the_string)
#
#
#
#
#
#



'''
QUESTION #17
You are given two lists of integers, and you need to compute their Cartesian product.

Input Format:
1. The first line contains an integer n, the number of integers in the first list.
2. The second line contains n space-separated integers.
3. The third line contains an integer m, the number of integers in the second list.
4. The fourth line contains m space-separated integers.

Constraints:
- 1 <= n, m <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the Cartesian product as a list of tuples.

Example Input:
3
1 2 3
2
4 5

Example Output:
[(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

Clues to Solve:
- Use nested loops to create all combinations of elements from both lists.
- Alternatively, use `itertools.product()` for a concise solution.
'''

#
#
# list_one = list(map(int, input('list_one: ').split()))
# list_two = list(map(int, input('list_two: ').split()))
#
#
# def compute_cartesian(in_list_one, in_list_two):
#     temp_list = []
#     for x in in_list_one:
#         for y in in_list_two:
#             temp_list.append((x,y))
#     return  temp_list
#
#
#
# print(compute_cartesian(list_one,list_two))
#
#
# # alternative
#
# from itertools import product
#
# def compute_cartesian(in_list_one, in_list_two):
#     return list(product(in_list_one, in_list_two))
#
# print(compute_cartesian(list_one, list_two))
#
#



'''
QUESTION #18
You are given a list of integers, and you need to check if all the elements in the list are unique.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print "YES" if all elements are unique, otherwise print "NO".

Example Input:
5
1 2 3 4 5

Example Output:
YES

Example Input:
5
1 2 3 4 1

Example Output:
NO

Clues to Solve:
- Use a set to check for duplicates.
- The size of the set will be equal to the size of the list if all elements are unique.
'''
#
#
# the_list = (list(map(int,input('the_list: ').split())))
#
#
# def is_unique(in_list):
#     the_set = set()
#     for x in in_list:
#         the_set.add(x)
#     if len(the_set) == len(in_list):
#         return True
#     else:
#         return False
#
# print(is_unique(the_list))


'''
QUESTION #19  
You are given a list of integers, and you need to find the element that appears the most frequently.  

Input Format:  
1. The first line contains an integer n, the number of integers in the list.  
2. The second line contains n space-separated integers.  

Constraints:  
- 1 <= n <= 10^3  
- -10^3 <= integer <= 10^3  

Output Format:  
Print the element that appears the most frequently.  
If there are ties, print the smallest element among the tied elements.  

Example Input:  
10  
1 2 3 1 2 2 3 3 3 1  

Example Output:  
3  

Clues to Solve:  
- How can you count occurrences of elements in the list efficiently?  
- What data structure would let you track counts?  
- How can you resolve ties using `min()` or sorting?  
(end)
'''



#
# the_list = list(map(int,input('the_list :').split()))
#
# def most_frequent(in_list):
#     # Step 1: Count occurrences
#     counts_nums = {}
#     for num in in_list:
#         # version one
#         #counts_nums[num] = counts_nums.get(num, 0) + 1
#
'''
        Look for the key num in the dictionary counts_nums:

If the key exists, get its current value (e.g., how many times num has been seen so far).
If the key doesn’t exist, return the default value 0 (since this is the first time we're seeing num).
Add 1 to this value:

If the key existed, its value is incremented by 1.
If the key didn’t exist, we add 1 to the default value 0, effectively setting it to 1.
Update the dictionary:

Assign the updated value (old value + 1) back to counts_nums[num].
If num wasn’t already in the dictionary, it gets created with an initial value of 1.
        '''
#
#         # version two
#         if num in counts_nums:  # the alternative_simpler version of above
#             counts_nums[num] += 1
#         else:
#             counts_nums[num] = 1
#
#
#
#
#
#     # Step 2: Find the most frequent number
#     most_frequent_num = max(counts_nums.items(), key=lambda x: (x[1], x[0]))
#
#     return most_frequent_num[0]
#
#
# print(most_frequent(the_list))
#
#
#
#
#
#
#
#
#


'''
QUESTION #20  
You are given a list of integers, and you need to find the longest sequence of consecutive integers in the list.  

Input Format:  
1. The first line contains an integer n, the number of integers in the list.  
2. The second line contains n space-separated integers.  

Constraints:  
- 1 <= n <= 1000  
- -1000 <= integer <= 1000  

Output Format:  
Print the length of the longest sequence of consecutive integers.  

Example Input:  
10  
1 9 3 10 2 20 4 1 5 6  

Example Output:  
6  

Clues to Solve:  
Remove Duplicates:  
Convert the list into a set to eliminate duplicate elements.  

Identify Sequence Starts:  
A number is the start of a sequence if the previous number, num - 1, is not present in the set.  

Check Consecutive Numbers:  
For every sequence start, use a loop to count how many consecutive numbers exist (num, num+1, num+2, etc.).  

Track Maximum Length:  
Store the longest sequence length encountered during the iteration.  

Output the Longest Sequence:  
At the end of the loop, print the maximum sequence length.  
'''

the_list = list(map(int,input('the_list :').split()))

def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums = set(nums)  # Remove duplicates
    max_length = 0

    for num in nums:
        # Check if `num` is the start of a sequence
        if num - 1 not in nums:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


print(longest_consecutive_sequence(the_list))


