class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        intutiion is the that we memoize.
        At each index we store max amount that can be robbed 
            which is max(nums[i]+dfs(i+2), dfs(i+1). 
        Make sure that in dfs we check if i > len(nums)
        
        '''
        n = len(nums)
        dp = {}
        def dfs(index):
            if index >= n:
                return 0
            if index in dp:
                return dp[index]
            temp = max(nums[index]+dfs(index+2),dfs(index+1))
            if index not in dp or temp < dp[index]:
                dp[index] = temp
            return dp[index]
        
        ret = dfs(0)
        return ret
