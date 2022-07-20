# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev = ListNode()
        dummy.next = cur = head
        while True:
            cnt = 0
            
            s = []
            while cur and cnt<k:
                cnt+=1
                s.append(cur)
                cur = cur.next
            
            if cnt == k:
                for _ in range(k):
                    prev.next = s.pop()
                    prev = prev.next
            
            else:
                prev.next = s[0] if s else None
                break

            prev.next = cur
                
        return dummy.next