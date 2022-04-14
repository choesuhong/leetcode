# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        global res
        
        res = None
        def find_unit(node):
            global res
            if node.val == val:
                res = node
                return res
            if node.left: find_unit(node.left)
            if node.right: find_unit(node.right)
                
        find_unit(root)
        return res