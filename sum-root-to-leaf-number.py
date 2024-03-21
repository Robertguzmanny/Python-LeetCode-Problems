# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # This method calculates the sum of all numbers formed by root-to-leaf paths in a binary tree.
    def sumNumbers(self, root):
        # Helper function for depth-first search (DFS) traversal of the tree.
        def dfs(cur, num):
            # Base case: if the current node is None, return 0 as we've reached beyond a leaf node.
            if not cur:
                return 0

            # Update the number formed by the current path by appending the current node's value.
            num = num * 10 + cur.val

            # If the current node is a leaf (no children), return the number formed up to this point.
            if not cur.left and not cur.right:
                return num

            # Recurse for both left and right children, adding their results together to accumulate the sum.
            # This effectively explores all paths from root to leaf, aggregating the sum of numbers formed.
            return dfs(cur.left, num) + dfs(cur.right, num)

        # Start the DFS traversal from the root with an initial number of 0.
        return dfs(root, 0)
#: O(N)
#: O(LogN) depending on the shape of the tree O(n)

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root.left = node2
root.right = node3
sol = Solution()
print(sol.sumNumbers(root))  # 25

