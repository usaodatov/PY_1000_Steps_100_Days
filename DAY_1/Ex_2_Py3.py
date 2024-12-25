'''
Question -1
You are given a list of integers, and you need to determine if the sum of the list is even or odd.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print "Even" if the sum of the list is even, otherwise print "Odd".

Example Input:
4
1 2 3 4

Example Output:
Even

Clues to Solve:
Calculate the sum of all numbers in the list.
Use the modulus operator to check the remainder when divided by 2.
If the remainder is 0, the sum is even; otherwise, it's odd.

How it works:
Input Reading:
Read n and the list of n integers from input.
Summing the List:
Use the sum() function to calculate the total sum of the list.
Determine Even/Odd:
Use a simple conditional check with % 2.
Output:
Print "Even" if the result is even or "Odd" if it is odd.
'''

from itertools import count

#code


# in_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
#
# # Take input as a space-separated string, split it into a list of strings,
# # convert each string to an integer, and create a new list of integers.
#
#
# def is_sum_even (sample_list):
#    sum_list= sum(sample_list)
#    if sum_list % 2 == 0:
#       print('even')
#    else:
#       print('odd')
#
#
# is_sum_even(in_list)
#



'''
Q2
You are given a list of integers, and you need to find and print the largest difference between any two elements in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 2 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the largest difference between any two elements.

Example Input:
5
1 2 9 4 5

Example Output:
8

Clues to Solve:
Find the maximum and minimum values of the list.
The largest difference is the absolute difference between the maximum and minimum values.

How it works:
Input Reading:
Read the size of the list (n) and the list of integers.
Find Extremes:
Use max() to find the maximum value and min() for the minimum value in the list.
Calculate Difference:
Compute the difference using the formula: max - mi

'''

#code

#
#
#
# def largest_difference(sample_list):
#    result =  max(sample_list) - min(sample_list)
#    print(result)
#
# in_list=  list(map(int, input('your list here:  ').split()))
#
# largest_difference(in_list)

'''
q3
You are given a list of integers, and you need to find and print the count of even and odd numbers in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print two integers separated by a space: the count of even numbers followed by the count of odd numbers.

Example Input:
6
1 2 3 4 5 6

Example Output:
3 3

Clues to Solve:
Iterate through the list to check each number.
Use the modulus operator to determine if a number is even or odd.
Increment separate counters for even and odd numbers.

How it works:
Input Reading:
Read the size of the list (n) and the list of integers.
Counting:
Use a loop to check each number using the % operator and increment counters for even and odd numbers.
Output:
Print the two counters as a single space-separated line.
'''

# #code
#
# input_list =  list(map(int, input('your list here:  ').split(" ")))
#
# def count_even_odd(sample_list):
#
#    list_odd = len([i for i in sample_list if i % 2 != 0])
#    list_even = len([i for i in sample_list if i % 2 ==0])
#    print('odds : ', list_odd)
#    print('evens : ',list_even)
#
# count_even_odd(input_list)
#
#


'''
q4

You are given a list of integers, and you need to find and print the sum of all unique elements in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the sum of all unique elements in the list.

Example Input:
6
1 2 2 3 4 4

Example Output:
8

Clues to Solve:
Remove duplicates from the list to get unique elements.
Use the set() function to eliminate duplicates efficiently.
Sum the elements of the resulting set.

How it works:
Input Reading:
Read the size of the list (n) and the list of integers.
Find Unique Elements:
Use the set() function to remove duplicates.
Calculate Sum:
Use the sum() function to add up the unique elements.
Output:
Print the resulting sum.
'''
#
#
# my_list= list(map(int, input('your list is here:  ').split()))
#
#
# def sum_of_all_unique_ints(sample_list):
#    unique_ints = set()
#
#    for i in sample_list:
#       unique_ints.add(i)
#
#
#    print(sum(unique_ints))
#
# sum_of_all_unique_ints(my_list)
#
#

'''
QUESTION # 5
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


#and you need to find and print the second smallest number


given_list = list(map(int,input('your list please:  ').split()))


def sec_smallest(input_list):
    acs_list = sorted(set(input_list))
    for i in range(len(acs_list)-1):
        if acs_list[i] != acs_list[i+1]:
            print(acs_list[i+1])
            break


sec_smallest(given_list)



#alternative with more improvement:

# def sec_smallest(input_list):
#     acs_list = sorted(set(input_list))  # Remove duplicates and sort the list
#     if len(acs_list) < 2:  # Check if there are at least two distinct elements
#         print("No second smallest number.")
#     else:
#         print(acs_list[1])  # Directly access the second smallest element
#
# given_list = list(map(int, input('your list please: ').split()))
# sec_smallest(given_list)







