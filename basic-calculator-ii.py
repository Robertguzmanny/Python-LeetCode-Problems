class Solution:
    def calculate(self, s):
        if not s:
            return 0

        # Initialize the stack, number, and operation
        stack, num, op = [], 0, '+'

        # Set of all operations for easy checking
        all_ops = {'+', '-', '*', '/'}

        # Add a padding right parenthesis to handle the last number
        s += '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in all_ops:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward zero
                # Reset the number and update the operation
                num, op = 0, s[i]

        # Sum up the numbers in the stack
        return sum(stack)

# Create a Solution object
sol = Solution()
# Example 1
input_str = "3+2*2"
output = sol.calculate(input_str)
print(output)
