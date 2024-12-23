# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      result = ListNode()
      cur = result
      has_ten = False
      while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        val = l1_val + l2_val + 1 if has_ten else l1_val + l2_val
        has_ten = True if val >= 10 else False
        val = val - 10 if has_ten else val
        cur.next = ListNode(val)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
      cur.next = ListNode(1) if has_ten else None
      return result.next