def merge_and_deduplicate_sorted_arrays(arr1, arr2, arr3):
    # Merge all arrays: Concatenate arr1, arr2, and arr3 into a single list
    # This combines all elements from the three input arrays into one larger array
    merged_array = arr1 + arr2 + arr3
    
    # Sort the merged array: Since the individual arrays are sorted but the combined
    # array might not be, we sort it to ensure all elements are in ascending order
    merged_array.sort()
    
    # Remove duplicates: Initialize an empty list to hold the unique elements
    unique_sorted_array = []
    
    # Use a variable to keep track of the previous element as we iterate through the sorted array
    # This is initialized to None since we haven't seen any element yet
    previous_element = None
    
    # Iterate through each element in the sorted, merged array
    for element in merged_array:
        # If the current element is not the same as the previous one, it's unique in our context
        if element != previous_element:
            # Add the unique element to the output array
            unique_sorted_array.append(element)
            # Update the previous element to be the current one for the next iteration
            previous_element = element
            
    # Return the array of unique, sorted elements
    return unique_sorted_array

# Example usage with comments explaining the test arrays
# Define three sorted arrays with some overlapping elements
arr1 = [1, 3, 5, 7]
arr2 = [1, 2, 4, 6, 8]
arr3 = [2, 3, 5, 7, 9]

# Call the function with the three arrays and store the result in a variable
# The function merges the arrays, sorts the combined array, and removes any duplicates
mergin_all_arrays = merge_and_deduplicate_sorted_arrays(arr1, arr2, arr3)

# Print the resulting array to verify the correct output
print(mergin_all_arrays)
