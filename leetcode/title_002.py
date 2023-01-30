# coding:utf8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        tail = head
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry

            if head:
                head = tail = ListNode(sum % 10)
            else:
                tail.next = ListNode(sum % 10)
                tail = tail.next

            carry = sum // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            print(tail.next)
        if carry > 0:
            tail.next = ListNode(carry)
        return head

    def maxSubArrayBF(nums):
        length = len(nums)
        MAX = nums[0]
        for i in range(0, length):
            for j in range(i + 1, length + 1):
                sub = nums[i:j]
                sub_sum = sum(sub)
                if sub_sum > MAX:
                    MAX = sub_sum
        return MAX


if __name__ == '__main__':
    # l1: ListNode = [2, 4, 3]
    # l2: ListNode = [5, 6, 4]
    # res = Solution.addTwoNumbers(l1, l2)
    # print(res)

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution.maxSubArrayBF(nums)
    print(res)
