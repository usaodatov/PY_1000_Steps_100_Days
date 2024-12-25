"""
  q1
    Question 1: String Manipulation
Write a Python function that takes a string as input and returns a dictionary.
The dictionary should have:

Keys as the unique characters in the string (case-sensitive).
Values as the count of occurrences of each character in the string.
Example:
Input: "HackerRank" Output: {'H': 1, 'a': 2, 'c': 1, 'k': 2, 'e': 1, 'R': 1, 'n': 1}
"""
#
# def count_chars(input_string):
#    the_dict = {}
#
#    for char in input_string:
#       if char in the_dict:
#          the_dict[char] += 1
#       else:
#          the_dict[char] = 1
#    print(the_dict)
#
#
# count_chars("HackerRank")


''''

q2
You are given a list of integers, and you need to determine if the list is sorted in non-decreasing order (ascending).

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print "YES" if the list is sorted in non-decreasing order. Otherwise, print "NO".

Example Input:
5
1 2 2 3 4

Example Output:
YES

Example Input:
5
1 3 2 4 5

Example Output:
NO

Clues to Solve:
- Use a loop to compare each pair of adjacent elements in the list.
- If any element is greater than the next, the list is not sorted.
- Alternatively, use Python's built-in sorted() function for a concise solution.

How it works:
Input Reading:
Read n and the list of integers from input.
Check Sorting:
Iterate through the list to ensure each element is less than or equal to the next.
Output:
Print "YES" or "NO" based on the result.
'''


# sample_list = list(map(int,input('your input LIST:  ').split()))
#
# def is_sorted_no_desc(this_list):
#    counter = 0
#    list_len = len(this_list)
#
#    for i in range(len(this_list)-1):
#
#       if this_list[i] > this_list[i+1]:
#          counter +=1
#
#    if counter == 0:
#       print('yes')
#    else:
#       print('no')
#
# '''
# #(further simplification)
#
# def is_sorted_no_desc(this_list):
#    for i in range(len(this_list) - 1):
#       if this_list[i] > this_list[i + 1]:  # Early exit on finding a violation
#          print('no')
#          return
#    print('yes')  # If no violations, the list is sorted
# '''

#ALT. WITH SORTED() METHOD

# def is_sorted_no_desc_alt(this_list):
#    if this_list == sorted(this_list):
#       print('yes')
#    else:
#       print('no')





#
# is_sorted_no_desc(sample_list)
# is_sorted_no_desc_alt(sample_list)


'''
You are given a list of integers, and you need to find the index of the first occurrence of the largest number in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print a single integer, the index (0-based) of the first occurrence of the largest number.

Example Input:
6
1 3 7 3 7 2

Example Output:
2

Clues to Solve:
- Use the max() function to find the largest number in the list.
- Use the index() method to find the index of the first occurrence of that number.

How it works:
Input Reading:
Read n and the list of integers.
Finding the Largest Number:
Use max() to determine the largest number in the list.
Finding the Index:
Use list.index() to find the index of its first occurrence.
Output:
Print the resulting index.
'''



#
#
# my_list = list(map(int, input('index of the first occurrence of the largest number. List plz  :  ').split()))
#
#
# def index_of_largest(in_list):
#    return in_list.index(max(in_list)) #index of the first occurrence of the largest number
#
#
# print(index_of_largest(my_list))
#
#
#
#
#
#
#
#

'''
QUESTION # 7
You are given a list of integers, and you need to rotate the list to the right by k positions.

Input Format:
1. The first line contains two integers n and k separated by a space:
   - n: the number of integers in the list.
   - k: the number of positions to rotate the list to the right.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- 0 <= k <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the rotated list as a space-separated string.

Example Input:
5 2
1 2 3 4 5

Example Output:
4 5 1 2 3

Clues to Solve:
- Rotating the list to the right by k positions means that the last k elements become the first k elements.
- Use slicing to achieve this efficiently:
  - The last k elements can be obtained with `list[-k:]`.
  - The rest of the list can be obtained with `list[:-k]`.
- Handle cases where k >= n by using `k % n` to avoid unnecessary rotations.

How it works:
Input Reading:
Parse n, k, and the list of integers.
Handle Rotations:
Use slicing to rearrange the list efficiently.
Output:
Print the rotated list as a space-separated string.
'''



#you need to rotate the list to the right by k positions

#
# list_int = [1,2,3,4,5,6,7,8,9]
# k = (2)
#
#
# def rotate_to_right_k(k_rotate_right):
#     #k_rotate_right = k_rotate_right % k
#     new_list = list_int[(len(list_int) - k_rotate_right) : ] + list_int[:(len(list_int) - k_rotate_right)]
#     print(new_list)
#
# rotate_to_right_k(k)

#alternatively  - negative back/right rotation

# list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = -2
#
# def rotate_to_right_k(k_rotate_right):
#     # k to handle both positive and negative
#     k_rotate_right = k_rotate_right % len(list_int)
#
#     # rotation
#     new_list = list_int[-k_rotate_right:] + list_int[:-k_rotate_right]
#     print(new_list)
#
# rotate_to_right_k(k)
#



'''
QUESTION # 8
You are given a string, and you need to count the number of vowels and consonants in it.

Input Format:
1. The input is a single string containing only alphabetic characters (uppercase and lowercase).

Constraints:
- 1 <= len(string) <= 10^3

Output Format:
Print two integers separated by a space: the number of vowels and the number of consonants.

Example Input:
hello

Example Output:
2 3

Clues to Solve:
- Vowels are 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase).
- Consonants are all other alphabetic characters except vowels.
- Iterate through the string and count vowels and consonants using conditional checks.
- Use the `lower()` method if needed to handle case insensitivity.

How it works:
Input Reading:
Accept a single string as input.
Classification:
Check each character to see if it’s a vowel or consonant.
Output:
Print the counts of vowels and consonants.
'''

#
# initial_input = input('only one word please:  ')
# initial_input = initial_input.lower()
# vowels_are =  ['a', 'e', 'i', 'o', 'u']
# vowels = 0
# consonants = 0
#
# for char in initial_input:
#     if char in vowels_are:
#         vowels += 1
#
#
# print(f'vowel = {vowels}, consonants = {len(initial_input)-vowels}')
#
#
#

'''
QUESTION # 9
You are given a string, and you need to determine if it is a palindrome.

Input Format:
- A single string containing only alphanumeric characters (case-insensitive).

Constraints:
- 1 <= len(string) <= 10^3

Output Format:
Print "YES" if the string is a palindrome, otherwise print "NO".

Example Input:
racecar

Example Output:
YES

Example Input:
hello

Example Output:
NO

Clues to Solve:
- A palindrome reads the same forwards and backwards.
- Ignore case while checking (e.g., "RaceCar" should be treated as "racecar").
- You can use slicing to reverse the string.
- Consider filtering out any non-alphanumeric characters if needed (e.g., "A man, a plan, a canal: Panama" should still be valid).

How it works:
Input Reading:
Read the string input.
Case Insensitivity:
Convert the string to lowercase to ignore case differences.
Check Palindrome:
Compare the string with its reversed version to determine if it's a palindrome.
Output:
Print "YES" or "NO" based on the result.
'''



# single_string = input('single string please  : ')
#
# if single_string.isalpha():
#
#     other_list = single_string[::-1]
#
#     if other_list == single_string:
#         print('yes')
#     else:
#         print('no')


# print(this_list)
# print(other_list)

'''
QUESTION # 10
You are given a list of integers, and you need to find and print the second smallest number.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 2 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the second smallest number.

Example Input:
6
1 2 2 3 4 5

Example Output:
2

Clues to Solve:
- Remove duplicates from the list to handle repeated elements.
- Sort the list in ascending order.
- The second smallest number will be the second element in the sorted list.

How it works:
Input Reading:
Parse the input to extract the list of integers.
Find Unique Values:
Use a set to remove duplicates.
Sort and Retrieve:
Sort the unique values in ascending order and retrieve the second element.
Output:
Print the second smallest number.
'''









