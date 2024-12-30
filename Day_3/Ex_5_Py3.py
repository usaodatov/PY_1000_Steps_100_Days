"""
QUESTION #21

You are given a list of integers, and you need to count how many duplicates exist in the list.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers.

Constraints:
- 1 <= n <= 10^5
- -10^5 <= integer <= 10^5

Output Format:
Print the number of integers that appear more than once in the list.

Example Input:
10
1 2 2 3 4 4 4 5 6 7

Example Output:
2

Clues to Solve:
- Use a dictionary to count the frequency of each integer.
- Identify keys with a frequency greater than 1 to find duplicates.
- Optimize for O(n) complexity by using a single pass to count frequencies.

How it works:
1. Input Reading:
   - Read the size of the list (n) and the list of integers.
2. Frequency Count:
   - Use a dictionary or collections.Counter to count occurrences of each number.
3. Filter Duplicates:
   - Iterate through the frequency dictionary and count how many integers have a count greater than 1.
4. Output Result:
   - Print the count of duplicate integers.

"""

# #the_list = list(map(int,input('the_list :').split()))
# test_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
#
# def how_many_dup(in_list):
#     the_dict={}
#     for num in test_list: # every number in the list , identify as a key
#         the_dict[num] = the_dict.get(num,0) + 1 #try to get it in the dict, if yes add one, or assign one.
#     count=0
#     for key,value in the_dict.items():
#         if value > 1: count+=1
#     return count
# print(how_many_dup(test_list))


"""
...
QUESTION #22  
You are given an array of integers and a target sum. Identify if there exists a 
subarray (a contiguous portion of the array) whose elements sum up to the given target.

Input Format:
1. The first line contains an integer n, the number of integers in the array.
2. The second line contains n space-separated integers representing the array.
3. The third line contains the target sum, an integer k.

Constraints:
1 <= n <= 10^5  
-10^3 <= array[i], k <= 10^3  

Output Format:
Print "YES" if such a subarray exists, otherwise print "NO".

Example Input:
6  
1 3 -2 5 -1 2  
4  

Example Output:
YES  

Clues to Solve:  
Sliding Window or Two-Pointer Approach:  
Use two pointers to maintain a subarray and calculate its sum in O(n).  
Adjust the start and end pointers based on the current sum compared to the target.

Hash Map for Cumulative Sum:  
Store cumulative sums in a dictionary.  
Check if current_sum - target exists in the dictionary, which indicates a subarray with the target sum.

How it works:  
1. Input Reading:  
Parse the size of the list (n), the list of integers, and the target sum.  

2. Cumulative Sum Technique:  
Maintain a current_sum while iterating through the array.  
Use a dictionary to store cumulative sums encountered.  
If current_sum - k exists in the dictionary, a subarray with the target sum is found.  

3. Output:  
Print "YES" if such a subarray exists, otherwise print "NO".  
...
"""

#
#
# test = {-2, -1, 1, 2, 3, 5}
#
# sorted_set = sorted((test))   #or just:  sorted_list = sorted
#
# max_length = 0
# searching_sequence = 4
#
# for num in sorted_set:
#     if num-1 not in sorted_set:   # determining if its start of the sequence
#         length =1
#         curr_num = num
#
#         while curr_num +1 in sorted_set:
#             length +=1
#             curr_num +=1
#
#         max_length = max(max_length,length)
#
# if max_length == searching_sequence: print('Yes')
# else: print('No')
#
# print(max_length)
#
#



'''
QUESTION #23

You are given a list of integers, and you need to rotate the list by a given number of steps to the right.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers, the elements of the list.
3. The third line contains an integer k, the number of steps to rotate the list.

Constraints:
- 1 ≤ n ≤ 10^5
- -10^3 ≤ integer ≤ 10^3
- 0 ≤ k ≤ 10^5

Output Format:
Print the rotated list as space-separated integers.

Example Input:
5
1 2 3 4 5
2

Example Output:
4 5 1 2 3

Clues to Solve:
1. **Modulo Optimization**:
   - If `k > n`, calculate `k % n` to reduce unnecessary rotations.
2. **Slicing**:
   - Use list slicing to separate the list into two parts and rearrange them.
3. **Iterative Approach**:
   - Rotate one step at a time using a loop for a simpler but less efficient solution.

How it works:
1. **Input Reading**:
   - Parse the size of the list (n), the list of integers, and the number of steps (k).

2. **Optimize Rotation Steps**:
   - Use `k % n` to calculate effective rotations if `k > n`.

3. **Perform the Rotation**:
   - Slice the list into two parts: the last `k` elements and the rest.
   - Concatenate them to form the rotated list.

4. **Output**:
   - Print the rotated list as space-separated integers.
'''



# the_list = list(map(int,input('the list  :  ').split()))
# the_k = int(input('the K  :  '))
#
# def rotate_t_right(in_list, k):
#     k = k % len(in_list)
#     return in_list[-k:] + in_list[:-k]
#
# print(rotate_t_right(the_list,the_k))



# alternative

def rotate_t_right_iterative(in_list, k):
    k = k % len(in_list)  # Handle cases where k > len(in_list) + how many times to pop() (last char in list)

    for _ in range(k):

        in_list.insert(0, in_list.pop())  # Remove the last element and insert it at the front

    return in_list


'''
QUESTION #24

You are given a list of integers, and you need to find all pairs of integers that sum up to a given target value.

Input Format:
1. The first line contains an integer n, the number of integers in the list.
2. The second line contains n space-separated integers, the elements of the list.
3. The third line contains an integer target, the target sum value.

Constraints:
- 2 <= n <= 10^5
- -10^3 <= integer <= 10^3
- -10^3 <= target <= 10^3

Output Format:
Print each pair of integers that sum up to the target value, one pair per line, in the order they appear. If no pairs exist, print "No pairs".

Example Input:
6
1 2 3 4 5 6
7

Example Output:
1 6
2 5
3 4

Clues to Solve:
1. Naive Approach:
   - Use two nested loops to check all pairs, but this is less efficient for larger inputs.
2. Optimized Approach Using a Set:
   - Use a set to store numbers you’ve seen so far.
   - For each number, check if `target - num` exists in the set.
3. Efficiency:
   - The set-based approach reduces the time complexity to O(n) instead of O(n^2).

How it works:
1. Input Reading:
   - Parse the size of the list (n), the list of integers, and the target value.
2. Check Pairs:
   - Iterate through the list and use a set to track numbers already seen.
   - For each number, check if its complement (target - num) exists in the set.
3. Store and Output Pairs:
   - If a pair is found, print it.
   - If no pairs exist after the loop, output "No pairs".
'''


#steps
'''
Sorting the List: nums.sort() sorts the input list.

Iterating through List: A loop iterates through each element, using it as the first element of the triplet.

Two Pointers: Two pointers (left and right) are used to find the remaining two elements that sum up to the target.

Skipping Duplicates: The code skips duplicates to ensure all triplets are unique.
'''



the_list = list(map(int, input('the list  :  ').split()))
the_value = int(input('the value  :  '))

def three_sum(nums, target):
    nums.sort()  # Sort the list to make it easier to find triplets
    result = []

    for i in range(len(nums) - 2):
        '''
        What it does: Loops through the list, fixing one number (nums[i]) at a time.
        Why it’s needed: To systematically try every number as the first number of the triplet.
        Purpose: Implements the main loop to iterate through potential triplets A + (B+C).
        '''

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        '''
        What it does: Skips duplicate numbers to avoid generating duplicate triplets.
        Why it’s needed: Prevents redundant calculations and ensures the output contains only unique triplets.
        Purpose: Ensures each number is considered only once as the first element of a triplet.
        '''

        left, right = i + 1, len(nums) - 1
        '''
        What it does: Initializes two pointers, left (just after i) and right (at the end of the list).
        Why it’s needed: Implements the two-pointer technique to efficiently find combinations of numbers.
        Purpose: Optimizes the search for valid triplets by reducing unnecessary iterations.
        '''

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            '''
            What it does: Calculates the sum of the three numbers at indices i, left, and right.
            Why it’s needed: This is the sum we compare to the target to decide whether to move the pointers or record the triplet.
            Purpose: Checks if the current triplet meets the condition.
            '''

            if total == target:
                '''
                What it does: Checks if the sum of the current triplet matches the target value.
                Why it’s needed: This is the primary condition for identifying valid triplets.
                Purpose: Validates whether the current triplet is a solution.
                '''
                result.append((nums[i], nums[left], nums[right]))
                '''
                What it does: Adds the current triplet as a tuple to the result list.
                Why it’s needed: Stores valid solutions for later output.
                Purpose: Collects all unique triplets.
                '''

                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                '''
                What it does: Moves the left pointer to skip duplicate values.
                Why it’s needed: Ensures the triplets in the result list are unique.
                Purpose: Avoids counting the same triplet multiple times.
                '''

                # Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                '''
                What it does: Moves the right pointer to skip duplicate values.
                Why it’s needed: Ensures the triplets in the result list are unique.
                Purpose: Avoids counting the same triplet multiple times.
                '''

                # Move both pointers inward to continue searching
                left += 1
                right -= 1

            elif total < target:
                '''
                What it does: Increases the left pointer if the current sum is less than the target.
                Why it’s needed: To try a larger value by moving to the next number in the sorted list.
                Purpose: Adjusts the search space to find a valid triplet.
                '''
                left += 1
            else:
                '''
                What it does: Decreases the right pointer if the current sum is greater than the target.
                Why it’s needed: To try a smaller value by moving to the previous number in the sorted list.
                Purpose: Adjusts the search space to find a valid triplet.
                '''
                right -= 1

    return result

print(three_sum(the_list, the_value))
