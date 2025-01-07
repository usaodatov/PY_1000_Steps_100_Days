Personal HackerRank Python Question Bank

Purpose
This repository is (my personal) a comprehensive collection of  Python coding exercises, inspired by challenges on platforms like HackerRank. It is designed to:
- Help learners systematically improve their Python skills.
- Serve as a resource for solving common programming problems.

The repository follows a structured approach with daily exercises. Each day's work is organized into separate folders (`DAY_1`, `DAY_2`, etc.), with 10 thoughtfully crafted coding problems. **As the days progress, the problems become increasingly complex, moving from foundational concepts to advanced Python techniques.**



Structure
Each folder (`DAY_1`, `DAY_2`, ...) contains:
-Problem Descriptions**: Detailed problem statements, input/output formats, constraints, examples, and clues to solve.
- Code Implementation**: Solutions in Python, including optimized approaches and step-by-step explanations in comments.



Problem Complexity Progression
- Day 1-7**: Focus on Python basics like conditional statements, loops, strings, and simple list operations.
- Day 8-15**: Introduce more advanced concepts like list comprehensions, set operations, and beginner-level algorithms.
- Day 16-25**: Cover object-oriented programming (OOP), functional programming, and intermediate-level algorithmic problems.
- Day 26-32**: Explore advanced topics such as regular expressions, data analysis with Pandas, web scraping, and debugging.



Example Problem Layout
Here’s a typical problem format in the files:


Question #1:
You are given a list of integers, and you need to determine if the sum of the list is even or odd.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Output Format:
Print "Even" if the sum of the list is even, otherwise print "Odd".

# Code implementation
def is_sum_even(sample_list):
    sum_list = sum(sample_list)
    if sum_list % 2 == 0:
        print('Even')
    else:
        print('Odd')

# Example Input
in_list = [1, 2, 3, 4]
is_sum_even(in_list)
