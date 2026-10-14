"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left
"""

class Solution:
    def isPalindrome(self, x: int) ->bool:
        s = str(x)
        return s == s[::-1]
    
# Test
solution = Solution()

result = solution.isPalindrome(1331)
print(result)