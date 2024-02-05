class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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



