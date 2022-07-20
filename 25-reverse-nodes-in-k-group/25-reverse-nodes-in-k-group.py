# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         dummy = prev = ListNode()
#         dummy.next = cur = head
#         while True:
#             cnt = 0
            
#             s = []
#             while cur and cnt<k:
#                 cnt+=1
#                 s.append(cur)
#                 cur = cur.next
            
#             if cnt == k:
#                 for _ in range(k):
#                     prev.next = s.pop()
#                     prev = prev.next
            
#             else:
#                 prev.next = s[0] if s else None
#                 break

#             prev.next = cur
                
#         return dummy.next
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next