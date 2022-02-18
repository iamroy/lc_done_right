#136. Single Number
#155. Min Stack
#70. Climbing Stairs
#206. Reverse Linked List
#169. Majority Element
#35. Search Insert Position
#389. Find the Difference

from collections import Counter
import math

#136. Single Number
def single_number(nums):
    return sum(set(nums)) - (sum(nums) - sum(set(nums)))

#155. Min Stack
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][1]

#206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, new_data):
        new_node = ListNode(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return

    def is_empty_linked_list(self):
        if self.head is None:
            return True
        else:
            return False

    def print_linked_list(self):
        if self.is_empty_linked_list():
            print('List is empty')
            return

        temp = self.head
        while temp:
            print(temp.val, end="=>")
            temp = temp.next
        print("None")



#70. Climbing Stairs
def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    i = 3
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return dp[n]

#169. Majority Element
def majority_element_hash_map(nums):
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)

def majority_element_sorted(nums):
    nums = sorted(nums)
    return nums[len(nums) // 2]

#35. Search Insert Position
def search_insert(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        pivot = (left+right)//2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot]>target:
            right = pivot-1
        else:
            left = pivot+1

    return left

def search_insert_recursive(nums, target, left, right):

    if left <= right:
        pivot = (left+right)//2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            return search_insert_recursive(nums, target, left, pivot-1)
        else:
            return search_insert_recursive(nums, target, pivot+1, right)
    else:
        return left

def search_insert_wrapper(nums, target):
    return search_insert_recursive(nums, target, 0, len(nums)-1)

#448. Find All Numbers Disappeared in an Array
# T: O(N), S: O(N)
def find_disappeared_numbers(nums):

    hash_map = {}
    out_list = []
    for num in nums:
        hash_map[num] = 1
    for num in range(1, len(nums)+1):
        if num not in hash_map:
            out_list.append(num)

    nums = sorted(nums)

    return out_list

def find_the_difference(s, t):
    hash_map = Counter(s)
    for c in t:
        if c not in hash_map or hash_map[c] == 0:
            return c
        else:
            hash_map[c] -= 1


if __name__ == '__main__':
    #nums = [2, 2, 1]
    #print(single_number(nums))
    #obj = MinStack()
    #obj.push(2)
    #obj.push(3)
    #obj.pop()
    #param_3 = obj.top()
    #param_4 = obj.getMin()
    #print(climb_stairs(45))
    #head = [1, 2, 3, 4, 5]

    #nums = [-1,1,1,1,2,1]
    #print(majority_element_hash_map(nums))
    #nums = [1, 2, 4, 5, 8, 10]
    #target = 7
    #print(search_insert(nums, target))
    #print(search_insert_wrapper(nums, target))
    #nums = [4, 3, 2, 7, 8, 2, 3, 1]
    #print(find_disappeared_numbers(nums))
    #print([i for i in range(1, len(nums)+1)])
    s = "abcd"
    t = "abcde"
    print(find_the_difference(s, t))