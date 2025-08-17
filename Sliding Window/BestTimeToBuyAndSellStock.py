# Date: August 17, 2025

class Solution(object):
   def maxProfit(self, prices):
       """
       :type prices: List[int]
       :rtype: int
       """
       # How to code this solution:
       # 1. Use two pointers - left (buy) and right (sell) starting at positions 0 and 1
       # 2. Move right pointer through array, calculating profit at each step
       # 3. If current price is higher than buy price, update max profit
       # 4. If current price is lower, move buy pointer to current position (better buy opportunity)
       # 5. This ensures we always buy low and sell high for maximum profit
       
       l, r = 0, 1  # Left pointer (buy), Right pointer (sell)
       maxP = 0     # Track maximum profit found
       
       while r < len(prices):
           if prices[l] < prices[r]:  # Profitable transaction possible
               profit = prices[r] - prices[l]
               maxP = max(maxP, profit)  # Update max profit if current is better
           else:
               l = r  # Found lower price, move buy pointer here
           r += 1     # Always move sell pointer forward
       
       return maxP
