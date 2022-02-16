#136. Single Number
#155. Min Stack
#70. Climbing Stairs
#206. Reverse Linked List


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

    def reverseList(self):
        if not self.head:
            return

        if self.head.next is None:
            return

        curr_node = self.head
        prev_node = None

        while curr_node.next:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        curr_node.next = prev_node

        self.head = curr_node

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


if __name__ == '__main__':
    nums = [2, 2, 1]
    #print(single_number(nums))
    obj = MinStack()
    obj.push(2)
    #obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    #print(climb_stairs(45))
    head = [1, 2, 3, 4, 5]
    myLinkedList = LinkedList()
    myLinkedList.append_node(1)
    myLinkedList.append_node(2)
    myLinkedList.append_node(3)
    myLinkedList.append_node(4)
    myLinkedList.append_node(5)
    print("Original Linked List")
    myLinkedList.print_linked_list()
    myLinkedList.reverseList()
    print("Reversed Linked List")
    myLinkedList.print_linked_list()