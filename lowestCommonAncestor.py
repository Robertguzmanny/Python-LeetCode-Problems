class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p,q)
        r = self.lowestCommonAncestor(root.right, p,q)

        if l and r:
            return root
        return l or r

# Step 1: Create the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Step 2: Select two nodes p and q
p = root.left  # Node with value 5
q = root.right  # Node with value 1

# Step 3: Call the lowestCommonAncestor method
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

# Step 4: Print the result
print(f"The LCA of nodes {p.val} and {q.val} is node with value {lca.val}.")