'''
QUESTION #11
You are given a list of integers, and you need to find and print the product of all elements in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the product of all integers in the list.

Example Input:
4
1 2 3 4

Example Output:
24

Clues to Solve:
- Use a loop to multiply all elements together.
- Start with a variable `product = 1`.
- Iterate through the list, updating the product at each step.
- If you want a concise approach, you can use `math.prod()` from Python's built-in `math` module.
    - To use `math.prod()`, you'll need to import it: `from math import prod`.
- If you're solving it manually with a loop, no additional modules are needed.

How it works:
Input Reading:
Parse the input to extract the list of integers.
Calculate the Product:
Multiply all numbers using a loop or math.prod().
Output:
Print the result.
'''
from itertools import count

# from math import prod
#
# the_list = list(map(int, input('the list please:  ').split()))
#
# def prod_list(in_list):  #math.prod([1, 2, 3, 4]))
#     print('The product of the list is: ',prod(in_list))
#
# prod_list(the_list)
#
#
#



'''
QUESTION #12
You are given a list of integers, and you need to determine how many of the integers are prime numbers.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- 1 <= integer <= 10^3

Output Format:
Print the count of prime numbers in the list.

Example Input:
6
1 2 3 4 5 6

Example Output:
3

Clues to Solve:
- Prime numbers are greater than 1 and divisible only by 1 and themselves.
- Create a helper function `is_prime(x)` to check if a number is prime.
- Use a loop or a list comprehension to count how many numbers in the list are prime.
- **No external modules are required.**
'''


# the_list = list(map(int, input('your list please: ').split()))
#
# def count_primes(in_list):
#     counter= 0
#
#     #helper function
#     def is_prime(n):
#         if n <= 1:  # Numbers <= 1 are not prime
#             return False
#         if n == 2:  # 2 is prime
#             return True
#         if not in_list: #case: user doesn’t provide any numbers
#             return 0
#
#         for i in range(2, int(n ** 0.5) + 1):  #to determine if any divisors exist upto int(n ** 0.5) + 1
#             if n % i == 0:
#                 return False
#         return True
#
#     #action - function
#     for num in in_list:
#         if is_prime(num):
#             counter += 1
#     return counter
#
# print(count_primes(the_list))

'''
QUESTION #13
You are given a list of integers, and you need to find and print the maximum difference between any two elements in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 2 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the maximum difference between any two elements in the list.

Example Input:
5
1 2 9 4 5

Example Output:
8

Clues to Solve:
- The maximum difference is the absolute difference between the smallest and largest elements.
- Use `min()` and `max()` to find the smallest and largest elements in the list.
- Calculate the difference using: `max_value - min_value`.
'''


#
#
# the_list = list(map(int, input('your list please: ').split()))
#
#
# def max_diff(the_list):
#     return max(the_list)-min(the_list)
#
# print(max_diff(the_list))
#




'''
QUESTION #14
You are given a list of integers, and you need to reverse the list without using the built-in `reversed()` function.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the reversed list as a space-separated string.

Example Input:
5
1 2 3 4 5

Example Output:
5 4 3 2 1

Clues to Solve:
- You can use list slicing to reverse the list: `list[::-1]`.
- Alternatively, use a loop to iterate through the list in reverse order and construct a new list.
'''

#
# the_list = list(map(int, input('your list please: ').split()))
#
# def reversed(the_list):
#     result_list = []
#     for i in range(len(the_list)-1,-1,-1):
#         result_list.append(the_list[i])
#     return result_list
#
#
#
# print(reversed(the_list))
#
#
#

'''
QUESTION #15
You are given a list of integers, and you need to find and print the sum of elements at even indices.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^3
- -10^3 <= integer <= 10^3

Output Format:
Print the sum of the elements at even indices.

Example Input:
6
1 2 3 4 5 6

Example Output:
9

Clues to Solve:
- Even indices in Python start from 0 and include 2, 4, 6, etc.
- Use a loop to iterate over the list and sum elements at even indices.
- Alternatively, use slicing (`list[::2]`) to extract elements at even indices and sum them.
'''


#
#
# in_list= [10,11,12,13,14,15,16,17,18]
#
# # the_list = list(map(int, input(' the list please: ').split()))
# #
# def sum_even_indices(in_list):
#
#     list_of_even_indices_element =[]
#     even_indices = list(range(0,len(in_list), 2))
#
#     for i in even_indices:
#         list_of_even_indices_element.append(in_list[i])
#         print(in_list[i])
#
#     result = sum(list_of_even_indices_element)
#     return result
#
#
# print(sum_even_indices(in_list))
#











