import collections
from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: # Defines a Solution class.
    def verticalOrder(self, root): 
        """
        Returns the vertical order traversal of a binary tree nodes.
        Time Complexity: O(N), where N is the number of nodes in the tree.
        Space Complexity: O(N), for storing the nodes in the queue and columns dictionary.
        """

        if not root: # Checks if the root node is None, indicating an empty tree.
            return [] # Returns an empty list for an empty tree.

        # Initializes a dictionary to map each vertical column index to a list of node values at that index.
        columns = collections.defaultdict(list) 

        # Initializes a double-ended queue with a tuple containing the root node and its horizontal distance (0).
        queue = collections.deque([(root, 0)]) 

        min_x = float('inf') # Initializes the minimum column index seen so far to positive infinity.
        max_x = float('-inf') # Initializes the maximum column index seen so far to negative infinity.

        res = [] # Initializes the result list to hold lists of node values for each vertical level.
        while queue: # Iterates as long as there are nodes to process in the queue.
            node, x = queue.popleft() # Removes and returns the leftmost item from the queue.
            
            # Adds the current node's value to the list of values at its column index.
            columns[x].append(node.val) 

            # Updates the minimum and maximum column indices seen so far.
            min_x = min(min_x, x) 
            max_x = max(max_x, x) 

            # If the current node has a left child, adds it to the queue with its column index decremented by 1.
            if node.left:
                queue.append((node.left, x - 1))
            # If the current node has a right child, adds it to the queue with its column index incremented by 1.
            if node.right:
                queue.append((node.right, x + 1))

        # Constructs the result list by iterating over the column indices from min_x to max_x.
        for level in range(min_x, max_x + 1):
            res.append(columns[level]) # Appends the list of node values at each column index to the result list.

        return res # Returns the result list containing the vertical order traversal.

root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

# Construct the tree
root.left = node9
root.right = node20
node20.left = node15
node20.right = node7

# Create a Solution instance and use it
sol = Solution()
vertical_order = sol.verticalOrder(root)

# Print the vertical order traversal of the binary tree
print(vertical_order)