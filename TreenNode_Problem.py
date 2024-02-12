class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# q: Given a binary tree, count the number of nodes in each value in python.
# The output should be a dictionary where the key is the value of the node and the value is the count of the number of nodes with that value.
# For example, given the following tree:
#     2
#    / \
#   1   3
#      / \
#     2   4
# Return {1: 1, 2: 2, 3: 1, 4: 1}

# A: We can use a depth-first search to traverse the tree and count the number of nodes for each value.
# We can use a dictionary to store the counts of each value. We can then traverse the tree and increment the count for each value we encounter.



def counting_nodes(root, counts):
    if root is None:
        return

    if root.value in counts:
        counts[root.value] += 1
    else:
        counts[root.value] = 1

    counting_nodes(root.left, counts)

    counting_nodes(root.right, counts)

def testing():
    root = TreeNode(2,
                    TreeNode(1),
                    TreeNode(3,
                             TreeNode(2),
                             TreeNode(4)))
    # Expected counts
    # expected_counts = {1: 1, 2: 2, 3: 1, 4: 1}

    # Actual counts
    actual_counts = {}
    counting_nodes(root, actual_counts)

    # Assert if actual counts match expected counts
    # assert actual_counts == expected_counts, f"Test failed! Expected {expected_counts}, got {actual_counts}"
    print(actual_counts)

# time and space O(n)

# Run the test case
testing()



