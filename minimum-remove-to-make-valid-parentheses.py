class Solution:
    #  O(n), where n is the length of the input string s.
    # the overall space complexity is O(n). The stack can also contain up to O(n) elements in the worst case if all opening parentheses are unmatched.
    def minRemoveToMakeValid(self, s: str) -> str:
        # Initialize a set to keep track of indices of parentheses to remove.
        indices_to_remove = set()
        # Use a stack to keep track of the indices of open parentheses '('.
        stack = []
        
        # First pass through the string to identify mismatched parentheses.
        for i, char in enumerate(s):
            if char == '(':
                # If the current character is an open parenthesis, push its index onto the stack.
                stack.append(i)
            elif char == ')':
                # If the current character is a closing parenthesis,
                if stack:
                    # and there is a matching open parenthesis in the stack, pop the stack.
                    stack.pop()
                else:
                    # If there is no matching open parenthesis, mark this index for removal.
                    indices_to_remove.add(i)
        
        # After processing all characters, any indices remaining in the stack are unmatched open parentheses.
        # Add these indices to the set of indices to remove.
        indices_to_remove = indices_to_remove.union(set(stack))
        
        # Construct the result string by including only those characters whose indices are not marked for removal.
        result = ''.join([s[i] for i in range(len(s)) if i not in indices_to_remove])
        
        # Return the cleaned string that now represents a valid parentheses sequence.
        return result

test = Solution()
s = ")("
print(f'{test.minRemoveToMakeValid(s)}')
