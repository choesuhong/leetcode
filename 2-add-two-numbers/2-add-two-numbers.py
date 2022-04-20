# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        zero = ListNode()
        node = zero.next
        st = [(l1, l2, zero)]
        rounded = 0
        while st:
            node1, node2, node = st.pop()
            
            val = 0
            
            if node1: val += node1.val
            if node2: val += node2.val
            val += rounded
            
            if val>9:
                rounded, val = 1, val%10
            else:
                rounded = 0
            
            node.next = ListNode(val=val)
            
            if node1.next or node2.next or rounded == 1:
                a = node1.next if node1.next else ListNode()
                b = node2.next if node2.next else ListNode()
                st.append((a, b, node.next))
            
        return zero.next