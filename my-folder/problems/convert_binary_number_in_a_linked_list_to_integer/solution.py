# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val_arr = []
        curr = head
        while curr is not None:
            val_arr.append(curr.val)
            curr = curr.next
        binary = ''.join(str(i) for i in val_arr)
        return int(binary, 2)