class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        same base intuition of hosue robber but with one distiction 
        sicne we cannot rob the first and last house together ever so we then create two sub arrays 
            the first sub array from 1st to second last element 
            the second sub array from 2nd to last element 
        then call the recursive funtion on btoh and see whihc is greater
        '''
        n = len(nums)
        if n ==1 :
            return nums[0]
        num1 = nums[0:n-1]
        num2 = nums[1:n]
        dp = {}
        dp2 ={}
        def dfs1(index):
            if index >= len(num1):
                return 0
            if index in dp:
                return dp[index]
            temp = max(num1[index]+dfs1(index+2),dfs1(index+1))
            if index not in dp or temp < dp[index]:
                dp[index] = temp
            return dp[index]
        def dfs2(index):
            if index >= len(num2):
                return 0
            if index in dp2:
                return dp2[index]
            temp = max(num2[index]+dfs2(index+2),dfs2(index+1))
            if index not in dp2 or temp < dp2[index]:
                dp2[index] = temp
            return dp2[index]
        
        ret1 = dfs1(0)
        ret2 = dfs2(0)
        
        return max(ret1,ret2)

        
        