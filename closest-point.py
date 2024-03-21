import heapq  # Import the heapq module to use as a min heap data structure.
class Solution:
    # Define the kClosest function which finds the k closest points to the origin.
    def kClosest(self, points, k):
        minHeap = []  # Initialize an empty list to use as a min heap.

        # Iterate through each point in the provided list of points.
        for x, y in points:
            # Calculate the distance of the point from the origin (0, 0) using the Euclidean distance formula, omitting the square root for efficiency as it doesn't affect the relative distances.
            dist = (x ** 2) + (y ** 2)
            # Append a list containing the distance and the point coordinates to the minHeap list. The distance is used as the first element to automatically sort the heap based on the distance.
            minHeap.append([dist, x, y])

        # Transform the minHeap list into a heap in-place, making the smallest distance element accessible at the heap's root.
        heapq.heapify(minHeap)
        res = []  # Initialize the result list to store the k closest points.

        # Loop to extract the k smallest elements (based on distance) from the minHeap.
        while k > 0:
            # Pop the smallest item from the heap, which is the point with the smallest distance to the origin. This operation also removes the item from the heap.
            dist, x, y = heapq.heappop(minHeap)
            # Append the x and y coordinates of the popped point to the result list.
            res.append([x, y])
            # Decrement k after each extraction to keep track of how many points we still need to find.
            k -= 1

        # Return the result list containing the coordinates of the k closest points to the origin.
        return res

test = Solution()
points = [[1,3],[-2,2]]
k = 1
print(test.kClosest(points, k)) # [[-2,2]]