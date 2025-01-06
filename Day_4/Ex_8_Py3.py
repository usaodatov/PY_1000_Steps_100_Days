'''
QUESTION #36

You are given two strings, and you need to determine if one is a rotation of the other.
 A string is a rotation of another if it can be obtained by moving some characters from the beginning of the string to the end.

Input Format:
1. The first line contains the first string.
2. The second line contains the second string.

Constraints:
- 1 <= len(string) <= 10^3
- Strings contain only lowercase alphabetic characters.

Output Format:
Print "YES" if the second string is a rotation of the first, otherwise print "NO".

Example Input:
waterbottle
erbottlewat

Example Output:
YES

Clues to Solve:
1. Concatenate the first string with itself to cover all possible rotations.
2. Check if the second string is a substring of the concatenated result.

How it works:
1. **Input Reading**:
   - Read the two strings.
2. **Concatenation**:
   - Concatenate the first string with itself. For example, "waterbottle" becomes "waterbottlewaterbottle".
3. **Substring Check**:
   - Check if the second string is a substring of the concatenated result.
4. **Output**:
   - Print "YES" if the second string is found, otherwise print "NO".
'''


#
# def is_substring(str_one,str_two):
#     # Concatenate the first string with itself to cover all possible rotations.
#     doubled_string = str_one + str_one
#
#     #check if the second string is a substring of the concatenated result.
#     # if the length of the two strings are equal and the second string is a substring of the doubled string
#     if len(str_one) == len(str_two) and str_two in doubled_string:
#         print('Yes')
#     else:
#         print('No')
#
#
#
# while True:  #  loop to keep the program running until the user decides to stop (optional)
#     # Read the two strings
#     string1 = input('word one:  ').strip()    # strip() removes any leading or trailing white spaces
#     string2 = input('word two:  ').strip()
#     is_substring(string1,string2) # call the function to check if the second string is a rotation of the first
#
#     to_continue = input('do you want to continue Y/N  :  ').lower()   #
#     if to_continue != 'y': # if the user enters anything other than 'y' the program will break
#         break
#
#
#
#


'''
QUESTION #37

You are given a string, and you need to determine whether it can be rearranged to form a palindrome.

Input Format:
- A single line containing a string.

Constraints:
- 1 <= len(string) <= 10^5
- The string contains only lowercase alphabetic characters.

Output Format:
- Print "YES" if the string can be rearranged to form a palindrome.
- Otherwise, print "NO".

Example Input:
aabbcc

Example Output:
YES

Example Input:
abc

Example Output:
NO

Clues to Solve:
1. Key Property of a Palindrome:
   A string can form a palindrome if at most one character has an odd frequency.
2. Efficient Frequency Count:
   Use a dictionary to count the frequency of each character.
3. Validation:
   Iterate through the frequency counts and count characters with odd frequencies.
   If more than one character has an odd frequency, the string cannot form a palindrome.

How it works:
1. Input Reading:
   Read the string as input.

2. Count Frequencies:
   Use a dictionary or collections.Counter to count occurrences of each character.

3. Validate Odd Counts:
   Check how many characters have an odd frequency.
   If only one or none have an odd frequency, it can form a palindrome.

4. Output the Result:
   Print "YES" if the conditions are met, otherwise print "NO".
'''

#
#
# from collections import Counter   # import the Counter class from the collections module
#
#
# my_string = input('possible Palindrome word:  ').strip()  # read from the user and rem leading or trailing white spaces
#
#
# def is_poss_palindrome(in_string):    # function to check if the string can be rearranged to form a palindrome
#
#     counter_values = Counter(in_string)  #  count the frequency of each character in the string
#     is_odd = sum(1 for freq in counter_values.values() if freq % 2 == 1) # check how many characters have an odd frequency
#
#
#     if len(in_string) % 2 == 1:              #if the length of the string is odd
#         if is_odd <= 1:                      #if there is at most one character with odd frequency
#             print('YES')
#         else:
#             print('NO')
#
#     else:                                    #if the length of the string is even
#         if is_odd == 0:                      #if there are no characters with odd frequency
#             print('Yes')
#         else:
#             print('No')
#
#
# is_poss_palindrome(my_string)
#
#
#


'''
QUESTION #38

You are given a string, and you need to count the frequency of each word in the string.

Input Format:
A single line containing a string of words separated by spaces.

Constraints:
- The string contains only alphabetic characters and spaces.
- 1 ≤ len(string) ≤ 10^3

Output Format:
Print each word and its frequency in the order they appear.

Example Input:
hello world hello python

Example Output:
hello 2
world 1
python 1

Clues to Solve:
- Split the string into a list of words using the split() method.
- Use a dictionary to store the frequency of each word.
- Iterate through the words in the list and update their count in the dictionary.

How it works:
1. **Input Reading**:
   - Accept a string of words as input.
2. **Split the String**:
   - Use split() to separate words into a list.
3. **Count Frequencies**:
   - Iterate through the list and update the frequency of each word in a dictionary.
4. **Outp

'''

#
#
# from collections import Counter   # import the Counter class from the collections module
#
# #User Input
# string_input = input('string_one  :').strip()  # read from the user and rem leading or trailing white spaces
#
#
# def count_how_many_of_each_word(in_string):  #  function to count the frequency of each word in the string
#     sentence_list = in_string.split(' ')     # split the string into a list of words using the split() method
#
#     count_freq = Counter(sentence_list)      # use a dictionary to store the frequency of each word.
#
#     return count_freq                        # return the dictionary of the frequency of each word
#
#
# print(count_how_many_of_each_word(string_input))  # print the dictionary of the frequency of each word
#

'''
You are given a string and need to determine the most frequently occurring word in the string.

Input Format:
1. The input is a single line containing a string.

Constraints:
- The string will contain only alphabetic characters and spaces.
- Words are case-insensitive (e.g., "Apple" and "apple" are considered the same).
- 1 ≤ length of the string ≤ 10^4.

Output Format:
Print the most frequent word and its count. If there are ties, print the lexicographically smallest word among the tied words.

Example Input:
apple banana apple orange apple banana orange

Example Output:
apple 3

Clues to Solve:
- Convert the string to lowercase to handle case insensitivity.
- Split the string into individual words using `split()`.
- Use a dictionary or `collections.Counter` to count the frequency of each word.
- Find the maximum frequency and resolve ties by sorting keys lexicographically.

How it works:
1. **Input Reading**:
   - Read the string and convert it to lowercase.
2. **Count Words**:
   - Use a `Counter` to count occurrences of each word in the string.
3. **Find the Most Frequent Word**:
   - Find the maximum value in the `Counter`.
   - Handle ties by finding the lexicographically smallest word among the tied words.
4. **Output**:
   - Print the most frequent word and its count.
'''
#
# from collections import Counter   # import the Counter class from the collections module
#
# input_string = input('string_one  :').strip().lower()  # read from the user and rem leading or trailing white spaces
#
# def most_frequent_word(in_string):  #  function to count the frequency of each word in the string
#     split_string = in_string.split(' ') # split the string into a list of words using the split() method
#     the_word_collection = Counter(split_string)     # use a dictionary to store the frequency of each word.
#
#     max_occur = max(the_word_collection.values()) # Find the maximum frequency of a word in the dictionary
#
#     # Find the lexicographically smallest word among the tied words.
#     most_frequent = sorted([word for word,freq in the_word_collection.items() if freq == max_occur])
#
#
#
#     # return the most frequent word and its count
#     return most_frequent[0]
#
# print(most_frequent_word(input_string))
#
#
#
#


'''
QUESTION #40

You are given a string, and you need to find the longest word in the string.

Input Format:
1. A single string containing multiple words separated by spaces.

Constraints:
- The string contains only alphabetic characters and spaces.
- Words are separated by a single space.
- 1 ≤ len(string) ≤ 10^3

Output Format:
Print the longest word in the string. If there are ties, print the word that appears first.

Example Input:
this is a comprehensive example string

Example Output:
comprehensive

Clues to Solve:
- Split the string into individual words using the split() method.
- Traverse through the list of words and find the one with the maximum length.
- Use the key parameter in the max() function to determine the longest word.
'''

input_string = input('string_one  :').strip().lower()  # read from the user and rem leading or trailing white spaces

def longest_word(in_string):  #  function to count the frequency of each word in the string
    split_string = in_string.split(' ') # split the string into a list of words using the split() method
    longest_word = max(split_string, key=len) # Find the longest word in the list of words

    return longest_word # return the longest word

print(longest_word(input_string)) # print the longest word

