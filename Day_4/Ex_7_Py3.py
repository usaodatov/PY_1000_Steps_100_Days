"""

""""""
QUESTION #31

You are given a string, and you need to determine whether it is a palindrome.

Input Format:
1. A single line containing a string.

Constraints:
- The string consists of only lowercase alphabetic characters.
- 1 ≤ len(string) ≤ 10^3

Output Format:
Print "YES" if the string is a palindrome, otherwise print "NO".

Example Input:
madam

Example Output:
YES

Clues to Solve:
1. **String Reversal**:
   - A string is a palindrome if it reads the same forward and backward.
   - Use slicing (`[::-1]`) to reverse the string and compare it to the original.

2. **Iterative Comparison**:
   - Alternatively, compare characters from the start and end of the string using a loop.

3. **Case Handling**:
   - Since input is guaranteed to be lowercase, no need for case adjustments.

How it works:
1. **Input Reading**:
   - Accept the string as input.
2. **Check for Palindrome**:
   - Compare the original string with its reversed version.
3. **Output**:
   - If they match, print "YES".
   - Otherwise, print "NO".
"""
from numpy.f2py.crackfortran import endifs

# # Accept the string as input
# sample_list = input('The word please  : ' ).lower()
#
# if not sample_list.strip():
#     print("Error: Input cannot be empty. Try again")
# elif not sample_list.isalpha():
#     print("Error: Only alphabetic characters. Try again.")
# else:
#     def is_palindrome(in_list):
#         if in_list[::-1] == in_list: return ('Yes')
#         else: return ('No')
#
#     print(is_palindrome(sample_list))
#
'''
QUESTION #32

You are given a string, and you need to determine whether it is a valid anagram of another string.

Input Format:
1. The first line contains the first string.
2. The second line contains the second string.

Constraints:
- Both strings consist of lowercase English letters only.
- 1 ≤ len(string) ≤ 10^5

Output Format:
Print "Yes" if the strings are anagrams of each other, otherwise print "No".

Example Input:
listen
silent

Example Output:
Yes

Clues to Solve:
1. **Sorting Approach**:
   - Anagrams contain the same characters in the same frequency.
   - Sort both strings and compare if they are identical.

2. **Frequency Count Approach**:
   - Use a dictionary or `collections.Counter` to count the frequency of each character in both strings.
   - Compare the two frequency counts.

3. **Edge Cases**:
   - Consider strings of different lengths (immediately not anagrams).
   - Handle strings with repeated characters.

How it works:
1. **Input Reading**:
   - Accept two strings from the user.

2. **Length Check**:
   - If the lengths of the two strings are not equal, they cannot be anagrams.

3. **Frequency Comparison**:
   - Use either sorting or frequency counting to compare the characters.

4. **Output Result**:
   - Print "Yes" if the strings are anagrams, otherwise print "No".
'''

# word_one = input(('word one  :'))
#
# word_two = input(('word two  :'))
#
# def is_anagram(word1, word2):
#    #stage one test condition - length
#     if len(word1) != len(word2):
#         return False
#
#     #stage two test condition - matching contents
#     word1_sorted = sorted(word1)
#     word2_sorted = sorted(word2)
#     return word1_sorted == word2_sorted
#
# # printing the result depending on is_anagram return
# if is_anagram(word_one, word_two):
#     print('Yes')
# else:
#     print('No')



#alternatively:

# word_one = input('word one  : ').lower()
# word_two = input('word two  : ').lower()
#
# def is_anagram(word1, word2):
#     # Check if lengths are equal
#     if len(word1) != len(word2):
#         return False
#
#     # Create frequency dictionaries for both words
#     char_count1 = {}
#     char_count2 = {}
#
#     # Count character frequencies for the first word
#     for char in word1:
#         char_count1[char] = char_count1.get(char, 0) + 1
#
#     # Count character frequencies for the second word
#     for char in word2:
#         char_count2[char] = char_count2.get(char, 0) + 1
#
#     # Compare the frequency dictionaries
#     return char_count1 == char_count2
#
# if is_anagram(word_one, word_two):
#     print('Yes')
# else:
#     print('No')


'''
QUESTION #33

You are given two strings, and you need to determine the longest common subsequence (LCS) between them.

Input Format:
1. The first line contains the first string.
2. The second line contains the second string.

Constraints:
- 1 ≤ length of strings ≤ 10^3
- Strings contain only lowercase alphabetic characters.

Output Format:
Print the longest common subsequence as a string. If there are multiple solutions, any valid one can be printed.

Example Input:
abcdef
acbcf

Example Output:
abcf

Clues to Solve:
1. **Dynamic Programming**:
   - Use a 2D table where `dp[i][j]` represents the LCS of the first `i` characters of the first string and the first `j` characters of the second string.
   - Build the table iteratively.
2. **Backtracking**:
   - After filling the `dp` table, backtrack to construct the LCS string.
3. **Optimization**:
   - Consider space optimization if memory usage becomes critical (e.g., using only two rows of the table).

How it works:
1. **Input Reading**:
   - Accept two strings as input.

2. **Initialize DP Table**:
   - Create a 2D list (`dp`) with dimensions `[len(string1) + 1][len(string2) + 1]`.
   - Initialize the first row and column to 0, as an LCS involving an empty string is empty.

3. **Fill DP Table**:
   - If characters match (`string1[i-1] == string2[j-1]`), update `dp[i][j] = dp[i-1][j-1] + 1`.
   - If characters don’t match, use the maximum value from `dp[i-1][j]` or `dp[i][j-1]`.

4. **Backtrack**:
   - Starting from `dp[len(string1)][len(string2)]`, trace back through the table to construct the LCS string.

5. **Output**:
   - Print the constructed LCS string.
'''

#
# def long_com_ss(in_list_a, in_list_b):
#     # Initialize DP table
#     dp = [[0] * (len(in_list_b) + 1) for _ in range(len(in_list_a) + 1)]   # 2D list with dimensions [len(string1) + 1][len(string2) + 1]
#
#     # Fill the DP table
#     for i in range(1, len(in_list_a) + 1):  # If characters match, update dp[i][j] = dp[i-1][j-1] + 1
#         for j in range(1, len(in_list_b) + 1):  # If characters don’t match, use the maximum value from dp[i-1][j] or dp[i][j-1]
#             if in_list_a[i - 1] == in_list_b[j - 1]: # If characters match, update dp[i][j] = dp[i-1][j-1] + 1
#                 dp[i][j] = dp[i - 1][j - 1] + 1 # If characters don’t match, use the maximum value from dp[i-1][j] or dp[i][j-1]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # If characters don’t match, use the maximum value from dp[i-1][j] or dp[i][j-1]
#
#     # Reconstruct LCS (optional)
#     lcs = []
#     i, j = len(in_list_a), len(in_list_b) #     Starting from dp[len(string1)][len(string2)], trace back through the table to construct the LCS string.
#     while i > 0 and j > 0:
#         if in_list_a[i - 1] == in_list_b[j - 1]: # If characters match, update dp[i][j] = dp[i-1][j-1] + 1
#             lcs.append(in_list_a[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]: # If characters don’t match, use the maximum value from dp[i-1][j] or dp[i][j-1]
#             i -= 1
#         else:
#             j -= 1
#
#     return ''.join(reversed(lcs))
#
#
#


'''
QUESTION #36

You are given a string, and you need to find the length of the longest substring that does not contain any repeated characters.

Input Format:
1. A single line containing the input string.

Constraints:
- 1 ≤ len(string) ≤ 10^5
- The string contains only printable ASCII characters.

Output Format:
Print the length of the longest substring without repeating characters.

Example Input:
abcabcbb

Example Output:
3

Clues to Solve:
1. **Sliding Window Technique**:
   - Use two pointers (or indices) to maintain a window of characters that does not contain duplicates.
2. **HashSet for Fast Lookup**:
   - Use a set to keep track of characters currently in the window.
3. **Update Window Dynamically**:
   - Move the left pointer to shrink the window if a duplicate character is found.
4. **Track Maximum Length**:
   - Update the maximum length whenever the window is adjusted.

How it works:
1. **Initialize Variables**:
   - Use two pointers (`left` and `right`) to define the sliding window.
   - Maintain a set to store characters in the current window.
   - Keep a variable to track the maximum length.

2. **Expand the Window**:
   - Move the `right` pointer to add characters to the window.
   - If a duplicate character is found, move the `left` pointer until the window is valid again.

3. **Update Maximum Length**:
   - Compare and store the maximum length whenever the window is adjusted.

4. **Output**:
   - Print the maximum length of the substring without repeating characters.
'''

# input('Enter the string  : ')
#
# def longest_substring(s):
#     left = 0
#     max_length = 0
#     char_set = set()
#
#     for right in range(len(s)): # Use two pointers to maintain a window of characters that does not contain duplicates.
#         while s[right] in char_set: # Use a set to keep track of characters currently in the window.
#             char_set.remove(s[left]) # Move the left pointer to shrink the window if a duplicate character is found.
#             left += 1 # Update the maximum length whenever the window is adjusted.
#
#         char_set.add(s[right]) # Move the right pointer to add characters to the window.
#         max_length = max(max_length, right - left + 1) # Compare and store the maximum length whenever the window is adjusted.
#
#     return max_length
#
# print(longest_substring(input('Enter the string  : ')))
#
#



'''
QUESTION #34

You are given a string, and you need to find the most frequently occurring character in the string. 
If there are multiple characters with the same frequency, return the lexicographically smallest one.

Input Format:
- A single line contains the string.

Constraints:
- The string contains only lowercase alphabetic characters.
- 1 ≤ len(string) ≤ 10^3

Output Format:
- Print the most frequently occurring character.

Example Input:
abracadabra

Example Output:
a

Clues to Solve:
1. **Count Character Frequencies:**
   - Use a dictionary to store the count of each character.
2. **Determine Maximum Frequency:**
   - Traverse the dictionary to find the character with the highest frequency.
3. **Handle Ties:**
   - If multiple characters have the same maximum frequency, choose the lexicographically smallest one.

How it works:
1. **Input Reading:**
   - Read the input string.
2. **Count Frequencies:**
   - Iterate through the string and count occurrences of each character.
3. **Find the Most Frequent Character:**
   - Compare frequencies and track the highest frequency while resolving ties using lexicographical order.
4. **Output:**
   - Print the most frequently occurring character.
'''
#
#
# def most_frequent(string): # Use a dictionary to store the count of each character.
#     if not string.strip():
#         return "Input string is empty!"
#
#     counter_dict = {} # Initialize an empty dictionary to store character frequencies.
#     for i in string:
#         counter_dict[i] = counter_dict.get(i, 0) + 1    # Count occurrences of each character.
#
#     max_key = min([k for k, v in counter_dict.items() if v == max(counter_dict.values())]) # Find the character with the highest frequency.
#     return max_key, counter_dict[max_key] # Return the most frequent character and its frequency.
#
#
# # Input
# in_string = input('in string:  ')
#
# # Output
# print(most_frequent(in_string))
#
#
#
#



'''
QUESTION #35

You are given a string, and you need to find the first non-repeating character in the string.

Input Format:
- A single string containing alphabetic characters (both uppercase and lowercase).

Constraints:
- 1 <= len(string) <= 10^5

Output Format:
- Print the first non-repeating character.
- If all characters repeat, print "None".

Example Input:
abracadabra

Example Output:
c

Clues to Solve:
1. **Build a Frequency Map**:
   - Use a dictionary to count the occurrences of each character.
2. **Iterate to Find the First Unique Character**:
   - Traverse the string to find the first character with a count of 1.
3. **Edge Cases**:
   - Handle cases where all characters repeat.
   - Consider case sensitivity if needed (e.g., "A" vs "a").
'''

# def first_non_repeating_char(s):  # Use a dictionary to count the occurrences of each character7

def first_non_repeating_char(s):  # Use a dictionary to count the occurrences of each character7
    if not s.strip(): # Return "None" if the input string is empty.
        return "None"

    char_count = {}  # Initialize an empty dictionary to store character frequencies.
    for char in s:

        char_count[char] = char_count.get(char, 0) + 1  # Count occurrences of each character.

    for char in s:  # Traverse the string to find the first character with a count of 1.
        if char_count[char] == 1:
            return char

    return "None"  # Return "None" if all characters repeat.


# Input
in_string = input('in string:  ')

# Output
print(first_non_repeating_char(in_string))




