class Solution:
    def numDecodings(self, s: str) -> int:
        '''
       This solution uses recursion with memoization (top-down DP) to solve the problem.
        The helper function `dfs(i)` calculates the number of ways to decode the string from index `i` to the end.
        At any index `i`, the total ways is the sum of possibilities: decoding one digit (`dfs(i+1)`) plus, if valid (10-26), decoding two digits (`dfs(i+2)`).
        The base case `dp[len(s)] = 1` is our "success" condition, signifying that one complete, valid decoding path has been found.
        '''
        dp ={len(s):1}
        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0
            
            res = dfs(i+1) 

            if i+1 != len(s): #if the next character in the len(s)
                if (s[i] == "1" and s[i+1] in "0123456789")   or (s[i] == "2" and s[i+1] in "0123456"):
                    res+=dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
            
        