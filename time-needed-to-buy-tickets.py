class Solution:
    def timeRequiredToBuy(self, tickets, k):
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])

            else:
               res += min(tickets[i], tickets[k] - 1)


        return res

test = Solution()
tickets = [5,1,1,1]
k = 0
print(test.timeRequiredToBuy(tickets, k))