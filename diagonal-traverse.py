from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Check for empty matrix
        if not mat or not mat[0]:
            return []

        # Get the number of rows and columns in the matrix
        rows, cols = len(mat), len(mat[0])
        # Initialize the result list to store the traversal order
        result = []
        # Initialize row and column indices for the traversal starting point
        row, col = 0, 0
        # Loop through all elements in the matrix
        for _ in range(rows * cols):
            # Append the current element to the result list
            result.append(mat[row][col])
            # Determine the direction of movement based on the sum of row and column indices
            # When moving up (sum of row and col is even)
            if (
                    row + col) % 2 == 0:  # (row + col) % 2 calculates the modulus (remainder) of the sum of the current row and column indices divided by 2.
                # If at the last column, move down to the next row
                if col == cols - 1:
                    row += 1
                # If at the first row, move right to the next column
                elif row == 0:
                    col += 1
                # Otherwise, move up diagonally
                else:
                    row -= 1
                    col += 1
            # When moving down (sum of row and col is odd)
            else:
                # If at the last row, move right to the next column
                if row == rows - 1:
                    col += 1
                # If at the first column, move down to the next row
                elif col == 0:
                    row += 1
                # Otherwise, move down diagonally
                else:
                    row += 1
                    col -= 1

        # Return the result list containing elements in their diagonal traversal order
        return result

test = Solution()

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(test.findDiagonalOrder(mat)) # [1,2,4,7,5,3,6,8,9]