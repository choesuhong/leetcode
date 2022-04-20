# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        zero = TreeNode(val=-1, right=root)
        st = [(root, zero)]
        
        while st:
            node, parent = st.pop()
            
            if not node:
                continue
            
            if node.val < low:
                if node.right: # right always exists
                    if node.right.val < parent.val:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                
                    st.append((node.right, parent))
                
                else:
                    if node.val < parent.val:
                        parent.left = None
                    else:
                        parent.right = None
                
                continue
            
            if node.val > high:
                if node.left: # left always exists
                    if node.left.val > parent.val:
                        parent.right = node.left
                    else:
                        parent.left = node.left
                    
                    st.append((node.left, parent))
                
                else:
                    if node.val < parent.val:
                        parent.left = None
                    else:
                        parent.right = None
                    
                continue
            
            st.append((node.left, node))
            st.append((node.right, node))
            
        return zero.right