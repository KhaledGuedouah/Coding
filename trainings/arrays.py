# Interview preparation practice module.
# Contains algorithms and data structure exercises for coding interviews.

from collections import deque

# Interview prep: this file groups common array problems with multiple solutions
# (brute force, optimized, and sometimes alternative approaches).
# Output: [0,1]
# Problem 1 — Two Sum

# Given an array of integers nums and an integer target, 
# return the indices of the two numbers such that they add up to target.
#
# 1 brut force O(n^2) O(1) 
def twosum_1(arr,target) :
    n = len(arr)
    if n==0 : return []
    for i in range (n):
        for j in range(i+1,n) :
            if (arr[i]+arr[j]==target) : 
                return [i,j]

# 2 two pointers  O(n) O(1) ======== two-pointer solution only applies to sorted arrays.
def twosum_2(arr,target) :
    if len(arr) == 0 : return []
    right = len(arr)-1
    left = 0
    while left != right : 
        if (arr[left]+arr[right]>target) : 
            right -= 1
        elif (arr[left]+arr[right]<target) : 
            left += 1
        else : 
            return [left,right]
    return [] 
            
# Hashmap O(n) O(n) 
def twosum_3(arr,target) :
    if len(arr) == 0 : return []
    seen = {}
    for i,num in enumerate(arr) : 
        complement = target - num
        if complement in seen : 
            return [seen[complement], i]
        else :
            seen[num] = i
    return []


def twosum(arr,target):
    if len(arr)==0 : return []
    seen = {}
    for idx,elem in enumerate(arr):
        comp = target - elem
        if comp in seen : 
            return [seen[comp],idx]
        else : 
            seen[elem]= idx 
    return []
    
    
    
# Round 6 — Arrays + Two Pointers
# Problem 6 — Move Zeroes

# Given an integer array nums, move all 0s to the end while maintaining 
# the relative order of non-zero elements

def movezeros(nums) : 
    res = []
    for num in nums : 
        if num != 0 : res.append(num)
    for _ in range(len(res),len(nums)) : 
        res.append(0)
    return res 
def movezeros2(nums) : 
    count = 0 
    for i in range(len(nums)) : 
        if nums[i] != 0 : 
            nums[count] = nums[i]
            count += 1 
    while count < len(nums) : 
        nums[count] = 0 
        count+=1 
    return nums 

def movezeros3(nums) : 
    count = 0 
    for i in range(len(nums)) : 
        if nums[i] != 0 : 
            nums[count] , nums[i]= nums[i], nums[count]
            count += 1 
    return nums 
     
# Problem 9 — Maximum Subarray (Kadane’s Algorithm)

# Given an integer array nums,
# find the contiguous subarray with the largest sum and return its sum.   
def maxSubarraySum(arr):  
    res = arr[0]
    for i in range(len(arr)) : 
        sum = 0  
        for j in range(i,len(arr)):
            sum += arr[j] 
            res = max(res, sum)
    return res    
 
# Kadane's Algorithm - O(n) Time and O(1) Space
def max_subarray_sum(arr):
    if not arr:
        return 0
    current_sum = max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def maxSubarraySum_(arr):  
    if not arr:
        return 0
    max_sum = current_sum = arr[0]
    start = end =  0 
    for i in range(1,len(arr)):
        if arr[i] >= current_sum + arr[i] : 
            current_sum =  arr[i]
            start = i
        else : 
            current_sum = current_sum + arr[i]
        if current_sum >= max_sum :
            max_sum = current_sum  
            end = i 
    return max_sum,arr[start:end+1] 
# Q1 — Why initialize with arr[0]?

# Because:
# arrays may contain all negative values

def findtarget(arr,target) : 
    if not arr : return -1 
    for i in range(len(arr)) : 
        if arr[i] == target : return i 
    return -1 
# O(log n) Time and O(1) Space
def findtarget_bs(arr,target) : 
    if not arr : return -1 
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        else : 
            high = mid-1
    return -1 
# O(log n) Time and O(Log n) Space
def findtarget_bs_r(arr,low,high,target) : 
    if not arr : return -1 
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < target:
            return findtarget_bs_r(arr,mid+1,high,target)
        else : 
            return findtarget_bs_r(arr,low,mid-1,target)
    else : return -1 
"""Q1 — Why:

mid=left+(right-left)/2



instead of:
mid=(left+right)/2



In C/C++:

left + right

may overflow integer range.

Very common systems interview question.


Why:
while left <= right

and not:

while left < right

ensures single-element intervals are checked.
"""

# Problem 12 — Sliding Window Maximum
# Given an array nums and a window size k, return the maximum value in each sliding window.


def sliding_max(nums,k):
    if not nums or k <= 0:
        return []
    maximums = []
    for i in range(len(nums)-k+1) : 
        max = nums[i]
        for j in range(i,i+k):
            if nums[j]> max : 
                max = nums[j]
        maximums.append(max)
    return maximums
def sliding_max(nums, k):
    if not nums or k <= 0:
        return []
    q = deque()   # stores indices
    result = []
    for i in range(len(nums)):
        print("q",q)
        print("result", result)
        # 1. Remove indices outside the current window
        while q and q[0] <= i - k:
            q.popleft()
        # 2. Remove smaller values from the back
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        # 3. Add current index
        q.append(i)
        # 4. Window is valid once i >= k - 1
        if i >= k - 1:
            result.append(nums[q[0]])
    return result


def sliding_max(nums, k):
    if not nums or k <= 0:
        return []
    result = [] 
    dq = deque()
    for i in range(len(nums)) : 
        # 1. Remove indices outside the current window
        while dq and dq[0] <= i - k : 
            dq.popleft()
        # 2. Remove smaller values from the back to keep the max at pos 0 of the q
        while dq and nums[i]>nums[dq[-1]] : 
            dq.pop()
        # 3. Add current index after removing smaller elements 
        dq.append(i)
        if i>= k-1 : 
            result.append(nums[dq[0]])
    return result 


# Problem 13 — Generate All Subsets

# Given an array of unique integers nums, return all possible subsets (the power set).
def subsets(arr) : 
    return [arr[i:j] for i in range(len(arr)) for j in range(i+1,len(arr)+1)]
def subsets_(arr) : 
    res = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            res.append(arr[i:j])
    return res 
def subsets(nums):

    result = []
    current = []

    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        # Choice 1: do not take nums[index]
        backtrack(index + 1)

        # Choice 2: take nums[index]
        current.append(nums[index])
        backtrack(index + 1)
        current.pop()

    backtrack(0)
    return result


# Problem 15 — Remove Duplicates from Sorted Array
# O(n) time complexity o(1) space complexity 
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[k-1] :
            nums[k] = nums[i]
            k+=1 
    return k, nums[:k]
# Time: O(n) Space: O(n) 
# Problem : a set does not preserve order 
def remove_duplicates(nums):
    if not nums:
        return 0
    return set(nums)
# Time: O(n) Space: O(n) 
def remove_duplicates(nums):
    if not nums:
        return 0
    return list(dict.fromkeys(nums))
# Worst case:
# Time: O(n²)
# Space: O(n)
# "x not in res" on a list is: O(n) , And you do it n times.
def remove_duplicates(nums): 
    res = []
    for x in nums:
        if x not in res :
             res.append(x)
    return res 

# Problem 17 — Find Duplicate Number
# Time: O(n)  Space: O(1)
def duplicatenum(nums) :
    slow = fast = 0 
    while True: 
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast : 
            break
    slow2 = 0
    while slow != slow2 : 
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow 
# Time: O(n)
# Space: O(n)
def duplicatenum(nums) :
    seen = {}
    for i,x in enumerate(nums) : 
        if x in seen : 
            return x 
        seen[x]=i 
        
# Time: O(n)
# Space: O(n)
def duplicatenum(nums) :
    seen = set()
    for x in nums : 
        if x in seen : 
            return x 
        seen.add(x) 
def duplicatenum(nums) :
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j] : 
                return nums[i]
    
if __name__ ==  '__main__' :

    nums = [2,7,11,15]
    target = 9
    arr = [0,1,0,3,12]
    # print(twosum_1(nums,target))
    # print(twosum_2(nums,target))
    # print(twosum_3(nums,target))
    # print(movezeros(arr))
    # print(movezeros2(arr))
    # print(movezeros3(arr))
    
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # print(maxSubarraySum_(nums))
    # nums = [-1,0,3,5,9,12]
    # target = 9
    # print(findtarget_bs(nums,target))
    
    # res = sliding_max(nums=[1,3,-1,-3,5,3,6,7],k=3)
    # print(res)
    
    print(subsets_([1,2,3]))
    print(subsets([1,2,3]))
    print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
    print(duplicatenum([1,3,4,2,2]) )


