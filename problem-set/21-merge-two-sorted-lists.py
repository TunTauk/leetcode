# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        is_list1_small = list1.val <= list2.val
        answer = ListNode(list1.val) if is_list1_small else ListNode(list2.val)
        temp = answer
        
        if is_list1_small:
            list1 = list1.next
        else:
            list2 = list2.next
            
        while list1 or list2:
            if not list1:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                temp = temp.next
                continue
            
            if not list2:
                temp.next = ListNode(list1.val)
                list1 = list1.next
                temp = temp.next
                continue
            
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
                temp = temp.next
                continue
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
        return answer