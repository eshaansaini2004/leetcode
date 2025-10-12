class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Okay so base case is if we reach the end then we return TRUE, WHY?
        recurrence relation is so check if basically 0<i<len(s)
            we need to check if s[0:i] is in wordDict and dfs(i+1) is true 
        
        

        wordSet = set(wordDict)
        def dfs(i):
            if i == len(s):
                return True 
            for j in range(i,len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        return True 
            else:
                return False
        return dfs(0)
        '''
        
        # dp solution
        '''
        so base case is if we reach the end then we return TRUE
         her we run thru each word in wordDict and check if s[i:i+len(w)] ==w and dfs(i+len(w)) is true
         if it is then we set dp[i] = True and return True
         if it is not then we set dp[i] = False and return False
         we then return dp[0]
         the dfs is just a wrapper to call the function with the index

         so basically we narrrow down the search portion by doing i+len(w) so see first if it fit withing 
         string s and thne we check if the substring is equal to current word in wordDict 
            If true then we call dfs(i+len(w)) and if that is true then we return true 
        '''
        dp = {len(s) : True}
        def dfs(i):
            if i in dp: 
                return dp[i]
            if i == len(s):
                return True

            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)] ==w:
                    if dfs(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)
