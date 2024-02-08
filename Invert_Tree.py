class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Manually construct the binary tree based on the given input
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

# Apply the invertTree method
solution = Solution()
solution.invertTree(root)

# Basic verification: Print the root and the first level of children
# to confirm inversion at the top level.
print("Root:", root.val)  # Expected: 4
print("Left Child of Root:", root.left.val)  # Expected: 7
print("Right Child of Root:", root.right.val)  # Expected: 2
# Optionally, print the second level of children if needed for further verification
