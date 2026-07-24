# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursively get max gain from left and right subtrees.
            # Discard negative gains (they'd only hurt the sum).
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Best path if this node is the "peak" (uses both branches)
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)

            # What we return upward: node can only extend ONE branch
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum