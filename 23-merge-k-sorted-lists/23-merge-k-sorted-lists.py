# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        
        while any(lists):
            mini = ListNode(val=10001)
            idx = -1
            for i in range(len(lists)):
                if lists[i] and mini.val>lists[i].val:
                    mini = lists[i]
                    idx = i
            cur.next, lists[idx] = mini, lists[idx].next
            cur = cur.next
        
        return dummy.next